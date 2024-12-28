// Bar Chart Example


// Fetch data from the API
fetch('/stockMonth') // Replace with your API URL
  .then(response => response.json())
  .then(data => {
    // Prepare the labels and data from the API response
    const labels = data.map(entry => entry.month);
    const dataset = data.map(entry => entry.total_folin_senhas);

var ctx = document.getElementById("gastusregional");
var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels:labels ,
    datasets: [{
      label: "Gastus Em Dolares",
      backgroundColor: "rgba(2,117,216,1)",
      borderColor: "rgba(2,117,216,1)",
      data: dataset,
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'month'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 6
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 1000,
          maxTicksLimit: 5
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
})
.catch(error => {
    console.error('Error fetching data:', error);
});
