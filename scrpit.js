document.addEventListener('DOMContentLoaded', function() {
    // Load Summary Data
    const summaryTableBody = document.getElementById('summary-data-table').getElementsByTagName('tbody')[0];

    fetch('data/summary_data.csv') // Ensure this path is correct
        .then(response => response.text())
        .then(data => {
            const rows = data.split('\n');
            for (let i = 1; i < rows.length; i++) {
                const cols = rows[i].split(',');
                if (cols.length > 1) { // Ensure valid row
                    const newRow = summaryTableBody.insertRow();
                    cols.forEach(col => {
                        const newCell = newRow.insertCell();
                        newCell.textContent = col; // Set cell text to the corresponding column value
                    });
                }
            }
        })
        .catch(error => {
            console.error('Error loading the summary CSV file:', error);
        });

    // Load Play Type Counts Data
    const playTypeTableBody = document.getElementById('play-type-table').getElementsByTagName('tbody')[0];

    fetch('data/play_type.csv') // Ensure this path is correct
        .then(response => response.text())
        .then(data => {
            const rows = data.split('\n');
            for (let i = 1; i < rows.length; i++) {
                const cols = rows[i].split(',');
                if (cols.length > 1) { // Ensure valid row
                    const newRow = playTypeTableBody.insertRow();
                    cols.forEach(col => {
                        const newCell = newRow.insertCell();
                        newCell.textContent = col; // Set cell text to the corresponding column value
                    });
                }
            }
        })
        .catch(error => {
            console.error('Error loading the play type counts CSV file:', error);
        });
});
