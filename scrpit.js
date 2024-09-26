// Sample data loading
document.addEventListener('DOMContentLoaded', function() {
    const tableBody = document.getElementById('data-table').getElementsByTagName('tbody')[0];

    fetch('data/summary_data.csv') // Ensure this path is correct
        .then(response => response.text())
        .then(data => {
            const rows = data.split('\n');

            // Start from the second row (index 1) to skip headers
            for (let i = 1; i < rows.length; i++) {
                const cols = rows[i].split(',');
                if (cols.length > 1) { // Ensure valid row
                    const newRow = tableBody.insertRow();

                    // Insert cells for each column in the row
                    cols.forEach(col => {
                        const newCell = newRow.insertCell();
                        newCell.textContent = col; // Set cell text to the corresponding column value
                    });
                }
            }
        })
        .catch(error => {
            console.error('Error loading the CSV file:', error);
        });
});
