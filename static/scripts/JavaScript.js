/**
 * Created by gunna on 18-6-2017.
 */
const CHART = document.getElementById("watertempLineChart");
console.log(CHART);
let lineChart = new Chart(CHART, {
    type: 'line',
    data: {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [
            {
                label: "Watertemperatuur",
                fill:false,
                lineTension: 0.1,
                backgroundColor:"rgba(75,192,192,0.4)",
                borderColor:"rgba(75, 192, 192, 1)",
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: "rgba(75, 192, 192, 1)",
                pointBackgroundColor: "#fff",
                pointBorderWidth: 1,
                pointHoverRadius: 5,
                pointHoverBackgroundColor:"rgba(75, 192, 192, 1)",
                pointHoverBorderColor: "rgba(0, 0, 0, 1)",
                pointHoverBorderWidth: 2,
                pointRadius: 1,
                pointHitRadius: 10,
                data: [65, 3, 20, 1, 75, 24, 90]
            }
        ]
    }
});

const CHART2 = document.getElementById("LuchtvochtigheidLineChart");
console.log(CHART2);
let lineChart2 = new Chart(CHART2, {
    type: 'line',
    data: {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [
            {
                label: "Luchtvochtigheid",
                fill:false,
                lineTension: 0.1,
                backgroundColor:"rgba(0,255,0,0.4)",
                borderColor:"rgba(0, 255, 0, 1)",
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: "rgba(0, 255, 0, 1)",
                pointBackgroundColor: "#fff",
                pointBorderWidth: 1,
                pointHoverRadius: 5,
                pointHoverBackgroundColor:"rgba(0, 255, 0, 1)",
                pointHoverBorderColor: "rgba(0, 0, 0, 1)",
                pointHoverBorderWidth: 2,
                pointRadius: 1,
                pointHitRadius: 10,
                data: [65, 59, 80, 81, 56, 55, 40]
            }
        ]
    }
});

const CHART3 = document.getElementById("TemperatuurLineChart");
console.log(CHART3);
let lineChart3 = new Chart(CHART3, {
    type: 'line',
    data: {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [
            {
                label: "Temperatuur kamer",
                fill:false,
                lineTension: 0.1,
                backgroundColor:"rgba(255,0,0,0.4)",
                borderColor:"rgba(255, 0, 0, 1)",
                borderCapStyle: 'butt',
                borderDash: [],
                borderDashOffset: 0.0,
                borderJoinStyle: 'miter',
                pointBorderColor: "rgba(255, 0, 0, 1)",
                pointBackgroundColor: "#fff",
                pointBorderWidth: 1,
                pointHoverRadius: 5,
                pointHoverBackgroundColor:"rgba(255, 0, 0, 1)",
                pointHoverBorderColor: "rgba(0, 0, 0, 1)",
                pointHoverBorderWidth: 2,
                pointRadius: 1,
                pointHitRadius: 10,
                data: [4, 2, 39, 50, 70, 60, 80]
            }
        ]
    }
});




