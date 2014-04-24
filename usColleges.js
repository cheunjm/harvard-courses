/**
 * plugin for slider
 * Created by hen on 3/8/14.
 */

// slider for enrollment

var colleges = new Array();
$(function() {
    $( "#slider-range1" ).slider({
      range: true,
      min: 0,
      max: 80000,
      values: [0, 80000],
      step: 5000,
      slide: function( event, ui ) {
        $( "#amount1" ).val(ui.values[ 0 ] + " - " + ui.values[ 1 ] );
      }
    });
    $( "#amount1" ).val($( "#slider-range1" ).slider( "values", 0 ) +
      " -" + $( "#slider-range1" ).slider( "values", 1 ) );
  });

// slider for tuition
$(function() {
    $( "#slider-range2" ).slider({
      range: true,
      min: 0,
      max: 50000,
      values: [0, 50000 ],
      step: 5000,
      slide: function( event, ui ) {
        $( "#amount2" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
      }
    });
    $( "#amount2" ).val( "$" + $( "#slider-range2" ).slider( "values", 0 ) +
      " - $" + $( "#slider-range2" ).slider( "values", 1 ) );
  });
var margin = {
    top: 50,
    right: 50,
    bottom: 50,
    left: 50
};

var width = 1060 - margin.left - margin.right;
var height = 650 - margin.bottom - margin.top;

var centered;
var mapVis = {
    x: 100,
    y: 10,
    w: width - 100,
    h: 300
};

var tableVisDimensions = {
    width: 230,
    height: 441
}

var plotVisDimensions = {
    width: 230,
    height: 200
}

 var canvas = d3.select("#mapVis").append("svg").attr({
    width: width + margin.left + margin.right - 150,
    height: height + margin.top + margin.bottom
    });
  var svg = canvas.append("g").attr({
          transform: "translate(" + (margin.left-80) + "," + margin.top + ")"
      });

var initial_nu_json, initial_nu_csv;
var initial_nlac_json, initial_nlac_csv;
var current_json, current_csv;

function loadColleges() {
    d3.json("../data/nu.json", function(error,data1){
        initial_nu_json = data1;
        d3.csv("../data/nu.csv", function(error,data2) {
            initial_nu_csv = data2
            d3.json("../data/nlac.json", function(error,data3){
              initial_nlac_json = data3;
                d3.csv("../data/nlac.csv", function(error,data4) {
                initial_nlac_csv = data4;
                colleges = Object.keys(initial_nu_json);
                current_json = initial_nu_json;
                current_csv = initial_nu_csv
                createVis(current_json,current_csv);
              });
           });
        });
    });
}

function createVis(jsonData,csvData) {
            createMap(jsonData);
            createTable(csvData);
            createPlot(csvData);
}

function destroyVis() {
  d3.select("#tableVis table").remove();
  d3.select("#plotVis svg").remove();
  d3.select("#mapVis").selectAll("circle").remove();
}

function createMap(jsonD) {

    // initialize basic map
    d3.json("../data/us-named.json", function(error, data) {
            var projection = d3.geo.albersUsa()
            .scale(1000)
            .translate([width / 2, height / 2]);

            var path = d3.geo.path()
                .projection(projection);

            svg.append("rect")
                .attr("class", "background")
                .attr("width", width)
                .attr("height", height)
                .on("click", clicked);

            var g = svg.append("g");
            
            var usMap = topojson.feature(data,data.objects.states).features;

            g.append("g")
                    .attr("id", "states")
                .selectAll(".country")
                    .data(usMap)
                .enter().append("path")
                    .attr("d", path)
                    .on("click", clicked);

            g.append("path")
                .datum(topojson.mesh(data, data.objects.states, function(a, b) { return a !== b; }))
                .attr("id", "state-borders")
                .attr("d", path);

                var mapData= d3.entries(jsonD);

                // tooltip
                 var tooltip = d3.select("body").append("div")
                  .attr("class", "tooltip")
                  .style("opacity", 0);

                var domainarray = [];
                for (i in mapData) {
                    if (mapData[i].value.size == null) {
                        domainarray.push(0);
                    }
                    else {
                        domainarray.push(mapData[i].value.size);
                    }
                }

                var colordomainarray = [];
                for (i in mapData) {
                    if (mapData[i].value.cost > 0) {
                        colordomainarray.push(mapData[i].value.cost);
                    }
                }  

                var scale = d3.scale.linear()
                    .domain(d3.extent(domainarray))
                    .range([2, 10]);

                // create color scale for circles based on cost
                var color = d3.scale.linear()
                .domain(d3.extent(colordomainarray))
                .interpolate(d3.interpolateRgb)
                .range(['white', 'blue']);

                // create legend
                colorlegend("#linearLegend", color, "linear", {title: "legend", linearBoxes: "9"});

                // create station circles
                g.selectAll("circles.points")
                .data(mapData)
                .enter()
                .append("circle")
                .on("click", function(d) {
                      highlightVis(d.key);
                    })
                    .on("mouseover", function(d) {
                      tooltip.transition()
                        .duration(200)
                        .style("opacity", 1)
                        .style("position", "absolute")
                        .style("border", "1px solid gray")
                        .style("background-color", "white")
                        .style("overflow", "hidden")
                        .style("z-index", "5");

                      tooltip.html(
                        d.value.rank + ". " + d.key + "<br />" +
                        "Enrollment: "+ d.value.size + "<br />" +
                        "Cost: $" + d.value.cost + "<br />" +
                        "Rate: " + d.value.rate + "%"
                        )
                      .style("left", (d3.event.pageX + 5) + "px")
                      .style("top", (d3.event.pageY - 55) + "px")
                      .style("font-size", "11px")
                      .style("padding", "3px");

                      d3.select(this)
                      .style("cursor", "pointer");

                    })
                    .on("mouseout", function(d) {
                      tooltip.transition()
                        .duration(200)
                        .style("opacity", 0);

                        d3.select(this)
                        .style("cursor", "normal");

                    })
                .attr("transform", function(d) {
                        return "translate(" + projection([d.value.location[1], d.value.location[0]]) + ")";
                })
                .attr("r",0)
                .transition()
                .duration(500)
                .attr("r", function(d) { return scale(d.value.size); })
                .attr("id", function(d){return d.key.toString().replace(/\W+/g,"")})

                .style("stroke", "#000")
                .style("fill", function(d) { return color(d.value.cost); });
                    
                    

        function clicked(d) {
          var x, y, k;

          if (d && centered !== d) {
            var centroid = path.centroid(d);
            x = centroid[0];
            y = centroid[1];
            k = 4;
            centered = d;
          } else {
            x = width / 2;
            y = height / 2;
            k = 1;
            centered = null;
          }

          g.selectAll("path")
              .classed("active", centered && function(d) { return d === centered; });

          g.transition()
              .duration(750)
              .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")scale(" + k + ")translate(" + -x + "," + -y + ")")
              .style("stroke-width", 1 / k + "px");
        }
        });

}

function createTable(data) {
        var name_sorted = false;
        var rank_sorted = true;
        var cost_sorted = false;
        var size_sorted = false; 
        var rate_sorted = false;     

        var table = d3.select("#tableVis").append("table"),
        thead = table.append("thead");
        tbody = table.append("tbody");

        var table_header = ["Name", "Rank", "Cost", "Size", "Rate"]
        
        thead.append("tr").selectAll("th")
        .data(table_header)
         .enter()
        .append("th")
        .text(function(d) { return d; })
        .attr("id", function (d,i) {
          if (i == 0){
            return "Name";
          }
          else if (i == 1){
            return "Rank";
          }
          else if (i == 2){
            return "Cost";
          }
          else if (i == 3){
            return "Size";
          }
          else {
            return "Rate";
          }
        })
        .style("font-size", "12px");

        // helper function that returns alternating colored rows
        function zebraRows(d, i) {
          if (i % 2 == 0) { return "lightgray"; }
          else { return "white"; }
        }

        var clicked = false;
        var clickedRow;

        // manipulate rows
        var rows = tbody.selectAll("tr")
        .data(data)
        .enter()
        .append("tr")
        .attr("id", function(d){return d.name.toString().replace(/\W+/g,"")})
        .style("background-color", function(d, i) { return zebraRows(d, i); })
        .on("mouseover", function(d, i) {
            d3.select(this)
            .style("cursor", "pointer");
        })
        .on("mouseout", function(d, i) {
            d3.select(this)
            .style("cursor", "normal");
        })
        .on("click", function(d, i) {
          highlightVis(d.name);

            // // a row has been clicked
            // if (clicked) {
            //     // clicked row that hasn't been already clicked
            //     if (i !== clickedRow) {
            //         // unhighlight prev row that had been clicked
            //         clickedRow = i;
            //         d3.selectAll("#tableVis table tr")
            //         .style("font-weight", "normal");
            //         // unhighlight corresponding point in mapVis and plotVis

            //         // highlight new row that has been clicked
            //         d3.select(this)
            //         .style("font-weight", "bold");
            //         // highlight corresponding point in mapVis and plotVis
            //     }
            //     // clicked row that has already been clicked
            //     else {
            //         clicked = false;
            //         d3.select(this)
            //         .style("font-weight", "normal");

            //         // unhighlight corresponding point in mapVis and plotVis
            //     }

            // }
            // // no row has been clicked yet
            // else {
            //     clicked = true;
            //     clickedRow = i;
            //     d3.select(this)
            //     .style("font-weight", "bold");

            //     // highlight corresponding point in mapVis and plotVis
            // }
        });

        // create cells for each row
        var cells = rows.selectAll("td")
        .data(function(row) {
          return d3.range(Object.keys(row).length).map(function(column, i) {
            return row[Object.keys(row)[i]];
          });
        })
        .enter()
        .append("td")
        .text(function(d) { return d; })
        .style("font-size", "10px")
        .style("text-align", "center");


        var column_class = rows.selectAll("td").attr("class", function(d,i) {return "col_" + i; }); 

        var name_cursor = function() { // changes in cursor for the state header
          d3.select("#Name").style("cursor", function() {
          if (name_sorted)
          {
            return "s-resize";
          }
          else{return "n-resize";}
        })};

        var rank_cursor = function() {  // changes in cursor for the rate header
        d3.select("#Rank").style("cursor", function() {
        if (rank_sorted)
        {
          return "s-resize";
        }
        else{return "n-resize";}
        })};

        var cost_cursor = function() {  // changes in cursor for the rate header
        d3.select("#Cost").style("cursor", function() {
        if (cost_sorted)
        {
          return "s-resize";
        }
        else{return "n-resize";}
        })};

        var rate_cursor = function() {  // changes in cursor for the rate header
        d3.select("#Rate").style("cursor", function() {
        if (rate_sorted)
        {
          return "s-resize";
        }
        else{return "n-resize";}
        })};

        var size_cursor = function() {  // changes in cursor for the rate header
        d3.select("#Size").style("cursor", function(){
        if (size_sorted)
        {
          return "s-resize";
        }
        else{return "n-resize";}
        })};

        // initializing all the functions so that they are functioning when the data is loaded
        name_cursor();
        rank_cursor();
        cost_cursor();
        size_cursor();
        rate_cursor();

        // sorting columns when state clicked
        var name_sort = thead.select("#Name").on("click", function (d,i) {
          rows.sort(function(a,b) {
            if(name_sorted) {
              b = [a, a = b][0];
            }
            return d3.ascending(a.name,b.name);           
          })
        .style("background-color", function(d, i) { return zebraRows(d, i); })

            name_sorted = !name_sorted; 
            name_cursor();
        });

        // sorting columns when rate clicked
        var rank_sort = thead.select("#Rank").on("click", function (d,i) {
          rows.sort(function(a,b) {
            if (rank_sorted){
                b = [a, a = b][0];
            }
            return d3.ascending(parseFloat(a.rank),parseFloat(b.rank));
            })
            .style("background-color", function(d, i) { return zebraRows(d, i); })

            rank_sorted = !rank_sorted; 
            rank_cursor();
        });

        var cost_sort = thead.select("#Cost").on("click", function (d,i) {
          rows.sort(function(a,b) {
            if (cost_sorted){
                b = [a, a = b][0];
            }
            return d3.ascending(parseFloat(a.cost),parseFloat(b.cost));
            })
            .style("background-color", function(d, i) { return zebraRows(d, i); })
            cost_sorted = !cost_sorted; 
            cost_cursor();
        });

        var size_sort = thead.select("#Size").on("click", function (d,i) {
          rows.sort(function(a,b) {
            if (size_sorted){
                b = [a, a = b][0];
            }
            return d3.ascending(parseFloat(a.size),parseFloat(b.size));
            })
            .style("background-color", function(d, i) { return zebraRows(d, i); })
            size_sorted = !size_sorted; 
            size_cursor();
        });

        var rate_sort = thead.select("#Rate").on("click", function (d,i) {
          rows.sort(function(a,b) {
            if (rate_sorted){
                b = [a, a = b][0];
            }
            return d3.ascending(parseFloat(a.rate),parseFloat(b.rate));
            })
            .style("background-color", function(d, i) { return zebraRows(d, i); })
            rate_sorted = !rate_sorted; 
            rate_cursor();
        });
}

function createPlot(data) {
    // insert scatterplot.html data here
    var margin = {top: 20, right: 20, bottom: 30, left: 40},
        width = 960 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    // var x = d3.scale.linear()
    //     .range([0, 280]);

    var x = d3.scale.pow().exponent(0.8).range([0, 280]); 

    var y = d3.scale.linear()
        .range([160, 0]);

    var color = d3.scale.category10();

    var xAxis = d3.svg.axis()
        .scale(x)
        .ticks(4)
        .orient("bottom");

    var yAxis = d3.svg.axis()
        .scale(y)
        .orient("left");

    var svg = d3.select("#plotVis").append("svg")
        .attr("width", 330)
        .attr("height", 200)
      .append("g")
        .attr("transform", "translate(50, 20)");

      data.forEach(function(d) {
        d.cost = +d.cost;
        d.size = +d.size;
      });

      // tooltip
    var tooltip = d3.select("#plotVis").append("div")
        .attr("class", "tooltip")
        .style("opacity", 0);

      x.domain(d3.extent(data, function(d) { return d.size; })).nice();
      y.domain(d3.extent(data, function(d) { return d.cost; })).nice();

      svg.append("g")
          .attr("class", "x axis")
          .attr("transform", "translate(0, 160)")
          .call(xAxis)
        .append("text")
          .attr("class", "label")
          .attr("x", 280)
          .attr("y", -6)
          .style("text-anchor", "end")
          .style("fill", "black")
          .text("Enrollment");

      svg.append("g")
          .attr("class", "y axis")
          .call(yAxis)
        .append("text")
          .attr("class", "label")
          .attr("transform", "rotate(-90)")
          .attr("y", 6)
          .attr("dy", ".71em")
          .style("text-anchor", "end")
          .style("fill", "black")
          .text("Cost")

    // color scale for points
        var color = d3.scale.linear()
        .domain(d3.extent(data, function(d) { return d.cost; }))
        .interpolate(d3.interpolateRgb)
        .range(['white', 'blue'])

    // create points for scatterplot
      svg.selectAll(".dot")
          .data(data)
        .enter().append("circle")
          .attr("id", function(d){return d.name.toString().replace(/\W+/g,"")})
          .attr("class", "dot")
          .attr("r", 3.5)
          .attr("fill", function(d) { return color(d.cost); })
          .attr("cx", function(d) { return x(d.size); })
          .attr("cy", function(d) { return y(d.cost); })
          .style("stroke", "#000")
          .on("click", function(d) {
            highlightVis(d.name);
          })
          .on("mouseover", function(d) {
            tooltip.transition()
                .duration(200)
                .style("opacity", 1)
                .style("position", "absolute")
                .style("border", "1px solid gray")
                .style("background-color", "white")
                .style("overflow", "hidden")
                .style("z-index", "5");

            tooltip.html(
                    d.rank+". "+d.name + "<br />" +
                    "Enrollment: "+ d.size + "<br />" +
                    "Cost: $" + d.cost + "<br />" +
                    "Rate: " + d.rate + "%")
              .style("left", (d3.event.pageX + 5) + "px")
              .style("top", (d3.event.pageY - 55) + "px")
              .style("font-size", "11px")
              .style("padding", "3px");

              d3.select(this)
              .style("cursor", "pointer");

            })
          .on("mouseout", function(d) {
                tooltip.transition()
                .duration(200)
                .style("opacity", 0);

                d3.select(this)
                .style("cursor", "normal");
            });
}
    
loadColleges();

function highlightVis(name){

  // highlight tableVis row
  d3.select("#tableVis").select("#"+name.toString().replace(/\W+/g,"")).style("font-weight", "bold");
  // highlight mapVis circle
  d3.select("#mapVis").select("#"+name.toString().replace(/\W+/g,"")).style("fill", "yellow");
  // highlight plotVis dot
  d3.select("#plotVis").select("#"+name.toString().replace(/\W+/g,"")).style("fill", "yellow");
}

function reset() {
  d3.selectAll("#tableVis table tr").style("font-weight", "normal");
  destroyVis();
  createVis(current_json, current_csv);
}

$("#reset").click(function() {
  reset();
})

$("#searchButton").click(function() {
  value = $("#search").val();
  highlightVis(value);
})

// function highlightSP (data) {
//   d3.select(#Yale)
// }

var nuClicked = true;

$("#nu").click(function() {
  if(!nuClicked){
    current_json = initial_nu_json;
    current_csv = initial_nu_csv;
    nuClicked = true;
    reset();
  }
})
$("#nlac").click(function() {
    if(nuClicked){
    current_json = initial_nlac_json;
    current_csv = initial_nlac_csv;
    nuClicked = false;
    reset();
  }
})

function updateData() {
  var enroll_range = d3.select("#amount1")[0][0].value.replace(/ /g,"").split("-");
  var tuition_range = d3.select("#amount2")[0][0].value.replace(/ /g,"").replace(/\$/g,"").split("-")
  filterJson(initial_nu_json, 0,0)
  // if(nuClicked){
  //   createVis(filterJson(initial_nu_json,enroll_range,tuition_range),filterCSV(initial_nu_csv,enroll_range,tuition_range))
  // }
}

function filterJson(jsonData,pop_range,cost_range){
  var ids = Object.keys(jsonData)
  console.log(ids);
}
