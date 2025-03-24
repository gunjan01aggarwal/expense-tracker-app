//for chart1 

// Get canvas element
const canvas = document.getElementById('myChart1');

if (canvas) {
    // Get the context
    const ctx1 = canvas.getContext('2d');

    new Chart(ctx1, {  // Use Chart instead of CharacterData
        type: 'line',
        data: {          
            labels: chartData1.labels1,
            datasets: [{
                label: "category",
                data: chartData1.values1,
                fill: false,
                borderColor: '#8A2BE2',
                tension: 0.1
            }]
        }
    });
} else {
    console.error("Canvas element with id 'myChart1' not found.");
}

/*new Chart(ctx1, {
    type: 'bar',
    data: {
        labels: chartData1.labels1,
        datasets: [{
            data: chartData1.values1,
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
                '#8A2BE2'  // Indigo
            ]
        }]
    },
    options: {
        responsive: true,
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
                    color: 'black',  // Change to desired color
                    font: {
                        size: 14,  // Adjust font size
                        weight: 'bold'
                    }   
                }
            },
            y: {  // Y-axis labels
                beginAtZero: true,
                ticks: {
                    color: 'black',  // Change to desired color
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
);*/

