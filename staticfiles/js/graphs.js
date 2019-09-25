Chart.defaults.global.elements.line.fill = false;
Chart.defaults.global.elements.line.tension = 0.0;
$.get('{% url "json1" %}', function(data) {
let ctx = $("#myChart1").get(0).getContext("2d");
new Chart(ctx, {
type: 'bar',
data: data,
options: {
title: {
display : true,
text : "Industry-Waste Distribution",
fontSize : 22.0
},
scales: {
yAxes: [{
scaleLabel: {
display: true,
labelString: 'Quantity of Waste',
fontSize : 20.0,
beginAtZero: true,
}
}],
xAxes: [{
scaleLabel: {
display: true,
labelString: 'Industries',
fontSize : 20.0,
}
}]
},
responsive: false,
legend: {
position:'top',
labels: {
padding: 20,
}
}
},
});
});

$.get('{% url "json2" %}', function(data) {
let ctx = $("#myChart2").get(0).getContext("2d");
new Chart(ctx, {
type: 'bar',
data: data,
options: {
title: {
display : true,
text : "NGO-Waste distribution",
fontSize : 22.0
},
scales: {
yAxes: [{
scaleLabel: {
display: true,
labelString: 'Quantity of Waste',
fontSize : 20.0,
beginAtZero: true,
}
}],
xAxes: [{
scaleLabel: {
display: true,
labelString: 'NGOs',
fontSize : 20.0,
}
}]
},
responsive: false,
legend: {
position:'top',
labels: {
padding: 20,
}
}
},
});
});

let endpoint1 = '/api/data1/';
let endpoint2 = '/api/data2/';
colors = ['#E35667','#E48857','#E3CE58','#ADE256','#69E257','#56E289','#57E2CD','#52AFEC','#5868E1','#8B56E2','#CD57DF','#E256AD'];
$.ajax({
method:'GET',
url: endpoint1,
success:function (data) {

new Chart(document.getElementById("myChart3"), {
type: 'pie',
data: {
labels: data.labels,
datasets: [{
label: "Quantity",
backgroundColor: colors,
data: data.mumbai,
}]
},
options: {
title: {
display: true,
text: 'Mumbai-Waste Distribution',
fontSize: 22.0
},
legend: {
position:'right',
labels: {
padding: 20,
}
},
}
});
new Chart(document.getElementById("myChart4"), {
type: 'pie',
data: {
labels: data.labels,
datasets: [{
label: "Quantity",
backgroundColor: colors,
data: data.delhi,
}]
},
options: {
title: {
display: true,
text: 'Delhi-Waste Distribution',
fontSize: 22.0
},
legend: {
position:'right',
labels: {
padding: 20,
}
},
}
});
new Chart(document.getElementById("myChart5"), {
type: 'pie',
data: {
labels: data.labels,
datasets: [{
label: "Quantity",
backgroundColor: colors,
data: data.hyderabad,
}]
},
options: {
title: {
display: true,
text: 'Hyderabad-Waste Distribution',
fontSize: 22.0
},
legend: {
position:'right',
labels: {
padding: 20,
}
},
}
});
new Chart(document.getElementById("myChart6"), {
type: 'pie',
data: {
labels: data.labels,
datasets: [{
label: "Quantity",
backgroundColor: colors,
data: data.bangalore,
}]
},
options: {
title: {
display: true,
text: 'Bangalore-Waste Distribution',
fontSize: 22.0
},
legend: {
position:'right',
labels: {
padding: 20,
}
},
}
});
new Chart(document.getElementById("myChart7"), {
type: 'pie',
data: {
labels: data.labels,
datasets: [{
label: "Quantity",
backgroundColor: colors,
data: data.trichy,
}]
},
options: {
title: {
display: true,
text: 'Trichy-Waste Distribution',
fontSize: 22.0
},
legend: {
position:'right',
labels: {
padding: 20,
}
},
}
});
},
error:function (error_data) {
console.log("error");
console.log(error_data);
},
});
$.ajax({
method:'GET',
url:endpoint2,
success:function(data) {
new Chart(document.getElementById("myChart8"), {
type: 'pie',
data: {
labels: data.labels,
datasets: [{
label: "Quantity",
backgroundColor: colors,
data: data.january,
}]
},
options: {
title: {
display: true,
text: 'January-Waste Distribution',
fontSize: 22.0
},
legend: {
position:'right',
labels: {
padding: 20,
}
},
}
});
new Chart(document.getElementById("myChart9"), {
type: 'pie',
data: {
labels: data.labels,
datasets: [{
label: "Quantity",
backgroundColor: colors,
data: data.february,
}]
},
options: {
title: {
display: true,
text: 'February-Waste Distribution',
fontSize: 22.0
},
legend: {
position:'right',
labels: {
padding: 20,
}
},
}
});
new Chart(document.getElementById("myChart10"), {
type: 'pie',
data: {
labels: data.labels,
datasets: [{
label: "Quantity",
backgroundColor: colors,
data: data.march,
}]
},
options: {
title: {
display: true,
text: 'March-Waste Distribution',
fontSize: 22.0
},
legend: {
position:'right',
labels: {
padding: 20,
}
},
}
});
new Chart(document.getElementById("myChart11"), {
type: 'pie',
data: {
labels: data.labels,
datasets: [{
label: "Quantity",
backgroundColor: colors,
data: data.april,
}]
},
options: {
title: {
display: true,
text: 'April-Waste Distribution',
fontSize: 22.0
},
legend: {
position:'right',
labels: {
padding: 20,
}
},
}
});
new Chart(document.getElementById("myChart12"), {
type: 'pie',
data: {
labels: data.labels,
datasets: [{
label: "Quantity",
backgroundColor: colors,
data: data.may,
}]
},
options: {
title: {
display: true,
text: 'May-Waste Distribution',
fontSize: 22.0
},
legend: {
position:'right',
labels: {
padding: 20,
}
},
}
});
new Chart(document.getElementById("myChart13"), {
type: 'pie',
data: {
labels: data.labels,
datasets: [{
label: "Quantity",
backgroundColor: colors,
data: data.june,
}]
},
options: {
title: {
display: true,
text: 'June-Waste Distribution',
fontSize: 22.0
},
legend: {
position:'right',
labels: {
padding: 20,
}
},
}
});
new Chart(document.getElementById("myChart14"), {
type: 'pie',
data: {
labels: data.labels,
datasets: [{
label: "Quantity",
backgroundColor: colors,
data: data.july,
}]
},
options: {
title: {
display: true,
text: 'July-Waste Distribution',
fontSize: 22.0
},
legend: {
position:'right',
labels: {
padding: 20,
}
},
}
});
new Chart(document.getElementById("myChart15"), {
type: 'pie',
data: {
labels: data.labels,
datasets: [{
label: "Quantity",
backgroundColor: colors,
data: data.august,
}]
},
options: {
title: {
display: true,
text: 'August-Waste Distribution',
fontSize: 22.0
},
legend: {
position:'right',
labels: {
padding: 20,
}
},
}
});
new Chart(document.getElementById("myChart16"), {
type: 'pie',
data: {
labels: data.labels,
datasets: [{
label: "Quantity",
backgroundColor: colors,
data: data.september,
}]
},
options: {
title: {
display: true,
text: 'September-Waste Distribution',
fontSize: 22.0
},
legend: {
position:'right',
labels: {
padding: 20,
}
},
}
});
new Chart(document.getElementById("myChart17"), {
type: 'pie',
data: {
labels: data.labels,
datasets: [{
label: "Quantity",
backgroundColor: colors,
data: data.october,
}]
},
options: {
title: {
display: true,
text: 'October-Waste Distribution',
fontSize: 22.0
},
legend: {
position:'right',
labels: {
padding: 20,
}
},
}
});
new Chart(document.getElementById("myChart18"), {
type: 'pie',
data: {
labels: data.labels,
datasets: [{
label: "Quantity",
backgroundColor: colors,
data: data.november,
}]
},
options: {
title: {
display: true,
text: 'November-Waste Distribution',
fontSize: 22.0
},
legend: {
position:'right',
labels: {
padding: 20,
}
},
}
});
new Chart(document.getElementById("myChart19"), {
type: 'pie',
data: {
labels: data.labels,
datasets: [{
label: "Quantity",
backgroundColor: colors,
data: data.december,
}]
},
options: {
title: {
display: true,
text: 'December-Waste Distribution',
fontSize: 22.0
},
legend: {
position:'right',
labels: {
padding: 20,
}
},
}
});
},
error:function(error_data){
console.log("error");
console.log(error_data);
},
});

