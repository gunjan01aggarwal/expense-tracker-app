//for chart2
// Get canvas element   

document.addEventListener("DOMContentLoaded", function () {

    const chartdata2 = JSON.parse(document.getElementById('chartdata2').textContent);

        if (chartdata2.labels2.length === 0 || chartdata2.values2.length === 0) {
            const canvasContainer = document.getElementById('myChart2');
            canvasContainer.outerHTML = '<p style="text-align:center; color: gray;">No data to display</p>';
        } else {
            const canvas2 = document.getElementById('myChart2');

            const ctx2=canvas2.getContext('2d');

            new Chart(ctx2, {
                type:'doughnut',
                data:{
                    labels: chartdata2.labels2,
                    datasets:[{
                        data: chartdata2.values2,
                        borderColor:'black',
                        borderWidth:2,            
                        backgroundColor:[
                            '#FF6384', // Red
                            '#36A2EB', // Blue
                            '#FFCE56', // Yellow
                            '#4BC0C0', // Teal
                            '#9966FF', // Purple
                            '#FF9F40', // Orange
                            '#8A2BE2',  // Indigo
                            '#FFD700', // Gold
                        ],
                        radius:'70%',
                        hoverOffset:4
                        
                    }]
                },
                options:{

                cutout:'50%',
            }   
                
        });
    }
});