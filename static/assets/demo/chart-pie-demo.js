// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
// Fetch data from the API
fetch('/transCat') // Replace with your API URL
  .then(response => response.json())
  .then(data => {
    // Prepare the labels and data from the API response
    const labels = data.map(item => item.categoria);
    const datasetData = data.map(item => item.total);
var ctx = document.getElementById("myPieChart");
    var myPieChart = new Chart(ctx, {
      type: 'pie',
      data: {
        labels: labels, // Set the labels dynamically
        datasets: [{
          data: datasetData, // Set the data dynamically
          backgroundColor: ['#007bff', '#dc3545', '#ffc107', '#28a745'], // Customize or map the colors dynamically if needed
        }],
      },
    });
  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });