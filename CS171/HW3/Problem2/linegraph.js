/**
 * Created by hen on 2/20/14.
 */
    var bbVis, brush, createVis, dataSet, handle, height, margin, svg, svg2, width, estimates;

    var fill = d3.scale.category10();
    var all_years=[];

    margin = {
        top: 50,
        right: 50,
        bottom: 50,
        left: 50
    };

    width = 960 - margin.left - margin.right;

    height = 300 - margin.bottom - margin.top;

    bbVis = {
        x: 0 + 100,
        y: 10,
        w: width - 100,
        h: 200
    };
    bbREsidual = {
        x: 100,
        y: 200,
        w: width,
        h: 100
    };
    estimates = [];
    var color = d3.scale.category10();
    var x = d3.scale.linear()
        .range([0, bbVis.w]);

    var y = d3.scale.linear()
            .range([bbVis.h, 0]);

    var xAxis = d3.svg.axis()
            .scale(x)
            .orient("bottom");

    var yAxis = d3.svg.axis()
            .scale(y)
            .orient("left")
            .ticks(4);;

    svg = d3.select("#vis").append("svg").attr({
        width: width + margin.left + margin.right,
        height: height + margin.top + margin.bottom
    }).append("g").attr({
            transform: "translate(" + margin.left + "," + margin.top + ")"
        });


    d3.csv("timeline.csv", function(data) {
            color.domain(d3.keys(data[0]).filter(function(key) {return key !== "year"; }));
            data.forEach(function(d) {
                if(all_years.indexOf(parseInt(d.year))== -1){
                    all_years.push(parseInt(d.year));
                }
                d.year = parseInt(d.year);
                d.USCensus = parseInt(d.USCensus);
                d.UN = parseInt(d.UN);
                d.PopulationBureau = parseInt(d.PopulationBureau);
                d.Maddison = parseInt(d.Maddison);
                d.HYDE = parseInt(d.HYDE);
            });

            estimates = color.domain().map(function(name) {
                return {
                  name: name,
                  values: data.map(function(d) {
                    return {year: d.year, population: +d[name], interpolated: false};
                  })
                };
            })
            console.log(estimates);
            estimates.forEach (function(m){
                m.values_noNaN = m.values.filter(function(a){return a.population >0})
                var min = d3.min(m.values_noNaN, function(v) { return v.year; });
                var max = d3.max(m.values_noNaN, function(v) { return v.year; });
                var temp_values = m.values.forEach(function(d,i){
                    if(isNaN(d.population) && (d.year > min) && (d.year < max)){
                        var lowerbound = 0
                        while(isNaN(m.values[i-lowerbound].population)){
                            lowerbound++;
                        }
                        var upperbound = 0
                        while(isNaN(m.values[i+upperbound].population)){
                            upperbound++;
                        }
                        var interp_scale = d3.scale.linear().domain([m.values[i-lowerbound].year,m.values[i+upperbound].year]).range([m.values[i-lowerbound].population,m.values[i+upperbound].population]);
                        d.population = interp_scale(d.year);
                        d.interpolated = true;
                    }
                });
                m.values = m.values.filter(function(a){return a.population >0});
            })
            console.log(estimates);
          x.domain(d3.extent(data, function(d) { return d.year; })); 
            y.domain([
            d3.min(estimates, function(c) { return d3.min(c.values, function(v) { return v.population; }); }),
            d3.max(estimates, function(c) { return d3.max(c.values, function(v) { return v.population; }); })
          ]);
        createVis();
    });

    createVis = function() {
       

        var line = d3.svg.line()
            .interpolate("basis")
            .x(function(d) { return x(d.year); })
            .y(function(d) { return y(d.population); });


		  var visFrame = svg.append("g").attr({
		      "transform": "translate(" + bbVis.x + "," + (bbVis.y + bbVis.h) + ")",
		  	  //....
			  
		  });
		  
		  visFrame.append("rect");

          visFrame.append("g")
          .attr("class", "x axis")
          // .attr("transform", "translate(0," + height + ")")
          .call(xAxis);

          visFrame.append("g")
              .attr("class", "y axis")
              .attr("transform", "translate(0,"+-1*bbVis.h+")")
              .call(yAxis)

           var estimate = visFrame.selectAll(".estimate")
              .data(estimates)
            .enter().append("g")
              .attr("class", "estimate");

          estimate.append("path")
              .attr("class", "line")
              .attr("d", function(d) { return line(d.values); })
              .style("stroke", function(d) { return color(d.name); })
              .attr("transform", "translate(0,"+-1*bbVis.h+")");

           for(var i = 0; i < estimates.length ; i++){
            visFrame.selectAll(".node " +estimates[i].name)
            .data(estimates[i].values.filter(function(d){return d.interpolated}))
              .enter().append("g")
            .attr("class",function(d){return "node " +estimates[i].name})
            .append("circle")
            .attr("r",3)
            .attr("fill", function(d){return color(estimates[i].name)})
            .attr("cx", function(d){return x(d.year)})
            .attr("cy", function(d){return y(d.population) - bbVis.h})

            visFrame.selectAll(".node " +estimates[i].name)
            .data(estimates[i].values.filter(function(d){return !d.interpolated}))
              .enter().append("g")
            .attr("class",function(d){return "node " +estimates[i].name})
            .append("rect")
            .attr("fill", function(d){return color(estimates[i].name)})
            .attr("x", function(d){return x(d.year)-2.5})
            .attr("y", function(d){return y(d.population) - bbVis.h-2.5})
            .attr("width",5)
            .attr("height",5 )
           }   
    };
