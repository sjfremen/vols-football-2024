// Sample data loading
document.addEventListener('DOMContentLoaded', function() {
    const tableBody = document.getElementById('data-table').getElementsByTagName('tbody')[0];

    fetch('data/your_data_file.csv')
        .then(response => response.text())
        .then(data => {
            const rows = data.split('\n');
            rows.forEach(row => {
                const cols = row.split(',');
                if (cols.length > 1) { // Ensure valid row
                    const newRow = tableBody.insertRow();
                    cols.forEach(col => {
                        const newCell = newRow.insertCell();
                        newCell.textContent = col;
                    });
                }
            });
        });
});
