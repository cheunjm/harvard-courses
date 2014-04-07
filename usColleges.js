/**
 * Created by hen on 3/8/14.
 */

var margin = {
    top: 50,
    right: 50,
    bottom: 50,
    left: 50
};

var width = 1060 - margin.left - margin.right;
var height = 800 - margin.bottom - margin.top;

var centered;
var bbVis = {
    x: 100,
    y: 10,
    w: width - 100,
    h: 300
};

var bbDetail = {
  width :350,
  height: 200
}

var detailVis = d3.select("#detailVis").append("svg").attr({
    width:bbDetail.width+margin.left + margin.right,
    height:bbDetail.height + margin.top + margin.bottom
})

var canvas = d3.select("#vis").append("svg").attr({
    width: width + margin.left + margin.right,
    height: height + margin.top + margin.bottom
    })

var svg = canvas.append("g").attr({
        transform: "translate(" + margin.left + "," + margin.top + ")"
    });

var focus = detailVis.append("g").attr({
        transform: "translate(" + margin.left + "," + margin.top + ")"
    });

var projection = d3.geo.albersUsa().translate([width / 2, height / 2]);//.precision(.1);
var path = d3.geo.path().projection(projection);

var completeDataSet = {};

function loadColleges() {

    d3.json("../data/college.json", function(error,data){
        completeDataSet= data;
        console.log(data);
        createTable();
    })

}
function createTable() {
}
    
  
loadColleges();
