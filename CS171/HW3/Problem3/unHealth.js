var bbDetail, bbOverview, dataSet, svg;

var margin = {
    top: 50,
    right: 50,
    bottom: 50,
    left: 50
};

var width = 960 - margin.left - margin.right;

var height = 800 - margin.bottom - margin.top;

bbOverview = {
    x: 0,
    y: 10,
    w: width,
    h: 50
};

bbDetail = {
    x: 0,
    y: 100,
    w: width,
    h: 300
};

dataSet = [];

var parseDate = d3.time.format("%b-%y").parse;

var x_overView = d3.time.scale().range([0, bbOverview.w]);

var x_Detail = d3.time.scale().range([0, bbDetail.w]);

var y_overView = d3.scale.linear().range([bbOverview.h, 0]);

var y_Detail = d3.scale.linear().range([bbDetail.h, 0]);

var xAxis_overView = d3.svg.axis()
    .scale(x_overView)
    .orient("bottom");

var xAxis_Detail = d3.svg.axis()
    .scale(x_Detail)
    .orient("bottom");

var yAxis_overView = d3.svg.axis()
    .scale(y_overView)
    .orient("left");

var yAxis_Detail = d3.svg.axis()
    .scale(y_Detail)
    .orient("left");    

var line_overView = d3.svg.line()
    .x(function(d) { return x_overView(d.date); })
    .y(function(d) { return y_overView(d.health); });

var line_Detail = d3.svg.line()
    .x(function(d) { return x_Detail(d.date); })
    .y(function(d) { return y_Detail(d.health); });    

var area = d3.svg.area()
    .x(function(d) { return x_Detail(d.date); })
    .y0(bbDetail.h)
    .y1(function(d) { return y_Detail(d.health); });

var brush = d3.svg.brush()
    .x(x_overView)
    .on("brush", brushed);     

svg = d3.select("#visUN").append("svg").attr({
    width: width + margin.left + margin.right,
    height: height + margin.top + margin.bottom
}).append("g").attr({
        transform: "translate(" + margin.left + "," + margin.top + ")"
    });

svg.append("defs").append("clipPath")
    .attr("id", "clip")
  .append("rect")
    .attr("width", width)
    .attr("height", height);

var visOverview = svg.append("g").attr({
              "transform": "translate(" + bbOverview.x + "," + (bbOverview.y + bbOverview.h) + ")"
          });
var visDetail = svg.append("g").attr({
              "transform": "translate(" + bbDetail.x + "," + (bbDetail.y + bbDetail.h) + ")"
          });

d3.csv("unHealth.csv", function(data) {
    data.forEach(function(d) {
    d.date = parseDate(d.date);
    d.health = +convertToInt(d.health);
    });
    console.log(data);  
    x_overView.domain(d3.extent(data, function(d) { return d.date; }));
    x_Detail.domain(d3.extent(data, function(d) { return d.date; }));
    y_overView.domain(d3.extent(data, function(d) { return d.health; }));
    y_Detail.domain(d3.extent(data, function(d) { return d.health; }));
  

    // bbOverview
    visOverview.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + bbOverview.h + ")")
      .call(xAxis_overView);

    visOverview.append("g")
      .attr("class", "y axis")
      .call(yAxis_overView)

    visOverview.append("path")
      .datum(data)
      .attr("class", "line")
      .attr("d", line_overView);

    visOverview.selectAll(".node ")
            .data(data)
            .enter().append("g")
            .attr("class",function(d){return "node"})
            .append("circle")
            .attr("r",2)
            .attr("cx", function(d){return x_overView(d.date)})
            .attr("cy", function(d){return y_overView(d.health)})   

    visOverview.append("g")
      .attr("class", "brush")
      .call(brush)
      .selectAll("rect")
      .attr({
        height: bbOverview.h,
        transform: "translate(0,0)"
      });

    svg.select(".background")
      .attr("height", bbOverview.h+20)  
     //bbDetail          
    visDetail.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + bbDetail.h  + ")")
      .call(xAxis_Detail);

    visDetail.append("g")
      .attr("class", "y axis")
      .call(yAxis_Detail)

    visDetail.append("path")
      .datum(data)
      .attr("class", "line")
      .attr("d", line_Detail);

    visDetail.append("path")
      .datum(data)
      .attr("class", "detailArea")
      .attr("d", area);  

    visDetail.selectAll(".node ")
            .data(data)
            .enter()
            .append("circle")
            .attr("class",function(d){return "node"})
            .attr("r",2)
            .attr("cx", function(d){return x_Detail(d.date)})
            .attr("cy", function(d){return y_Detail(d.health)})      
    d3.select(".fpeak")
    .on("click", function(){
        console.log(x_overView(parseDate("Feb-11")));
        brush.extent([parseDate("Feb-10"), parseDate("Feb-11")]);
        svg.select(".brush").call(brush);
    });
    d3.select(".fpeak")
    .on("click", function(){
        brush.extent([parseDate("Jan-12"), parseDate("Mar-12")]);
        svg.select(".brush").call(brush).call(brush.event);
        brushed;
    });         
    d3.select(".speak")
    .on("click", function(){
        brush.extent([parseDate("Jul-12"), parseDate("Sep-12")]);
        svg.select(".brush").call(brush).call(brush.event);
    });             
});

function brushed() {
  x_Detail.domain(brush.empty() ? x_overView.domain() : brush.extent());
  visDetail.select(".detailArea").attr("d", area);
  visDetail.select(".line").attr("d",line_Detail);
  visDetail.selectAll("circle")
            .attr("cx", function(d){return x_Detail(d.date)})
            .attr("cy", function(d){return y_Detail(d.health)}); 
  visDetail.select(".x.axis").call(xAxis_Detail);
}

var convertToInt = function(s) {
    return parseInt(s.replace(/,/g, ""), 10);
};

