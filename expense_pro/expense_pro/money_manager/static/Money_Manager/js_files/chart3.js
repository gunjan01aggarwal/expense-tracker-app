//for chart1 
// Get canvas element
document.addEventListener("DOMContentLoaded", function () {

    const chartdata3 = JSON.parse(document.getElementById('chartdata3').textContent);

        if (chartdata3.labels3.length === 0 || chartdata3.values3.length === 0) {
            const canvasContainer = document.getElementById('myChart3');
            canvasContainer.outerHTML = '<p style="text-align:center; color: gray;">No data to display</p>';

            /*document.getElementById('myChart3').innerHTML = '<p style="text-align:center; color: gray;">No data to display</p>';*/
        } else {
            const canvas3 = document.getElementById('myChart3');

            // Get the context
            const ctx3 = canvas3.getContext('2d');

            new Chart(ctx3, {
                type: 'bar',
                data: {
                    label: 'Monthly Expenses',
                    labels: chartdata3.labels3,
                    datasets: [{
                        data: chartdata3.values3,
                        barThickness: 40, 
                        borderColor: 'black',
                        borderWidth: 2,
                        backgroundColor: [
                            '#FF6384', // Red
                            '#36A2EB', // Blue
                            '#FFCE56', // Yellow
                            '#4BC0C0', // Teal
                            '#9966FF', // Purple
                            '#FF9F40', // Orange
                            '#8A2BE2',  // Indigo
                            '#FFD700', // Gold
                            '#FF6347', // Tomato
                            '#FF00FF', // Fuchsia
                            '#00FF00', // Lime
                            '#00FFFF', // Aqua
                        ]
                    }]
                },
                options: {
                    maintainAspectRatio: false,
                    layout: {
                        padding: {
                            left: 20,   // Padding from left
                            right: 20,  // Padding from right
                            top: 20,    // Padding from top
                            bottom: 0  // Padding from bottom
                        }
                    },
                    scales: {
                        x: {  // X-axis labels
                            ticks: {
                                color: 'red',  // Change to desired color
                                font: {
                                    size: 14,  // Adjust font size
                                    weight: 'bold'
                                }   
                            }
                        },
                        y: {  // Y-axis labels
                            beginAtZero: true,
                            ticks: {
                                color: 'red',  // Change to desired color
                                font: {
                                    size: 14, 
                                    weight: 'bold'
                                }
                            }
                        }
                    },
                    plugins:{
                        legend:{
                            display: false
                        }
                    },
                    animation:{
                            duration: 2000,
                            easing: 'easeInOutQuad'
                    }
                }
            }
            )};
});
