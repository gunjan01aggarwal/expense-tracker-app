//for chart2
// Get canvas element   
const canvas2 = document.getElementById('myChart2');

const ctx2=canvas2.getContext('2d');

new Chart(ctx2, {
    type:'doughnut',
    data:{
        labels: chartData2.labels2,
        datasets:[{
            data: chartData2.values2,
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