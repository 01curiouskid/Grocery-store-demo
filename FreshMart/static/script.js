document.querySelector('form').addEventListener('submit', function(event) {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const role = event.submitter.value;

    if (role === 'admin' && (username !== 'admin' || password !== 'admin')) {
        event.preventDefault();
        alert('Incorrect Admin credentials!');
    }
});

// Function to open the edit popup
function openEditPopup(id, costPerUnit, quantityLeft) {
    document.getElementById('edit-item-id').value = id;
    document.getElementById('edit-cost-per-unit').value = costPerUnit;
    document.getElementById('edit-quantity-left').value = quantityLeft;
    document.getElementById('edit-popup').style.display = 'block';
}

// Function to open the add new item popup
function openAddPopup() {
    document.getElementById('add-popup').style.display = 'block';
}

// Function to close pop-ups
function closePopup(popupId) {
    document.getElementById(popupId).style.display = 'none';
}

// Close popups when clicking outside of them
window.onclick = function(event) {
    if (event.target.className === 'popup') {
        event.target.style.display = 'none';
    }
}
document.getElementById('orders-btn').addEventListener('click', function() {
    document.getElementById('orders-section').style.display = 'block';
    document.getElementById('inventory-section').style.display = 'none';
});

document.getElementById('inventory-btn').addEventListener('click', function() {
    document.getElementById('orders-section').style.display = 'none';
    document.getElementById('inventory-section').style.display = 'block';
});

function openEditModal(id, cost, quantity) {
    document.getElementById('edit-modal').style.display = 'block';
    document.getElementById('item-id').value = id;
    document.getElementById('cost-per-unit').value = cost;
    document.getElementById('quantity-left').value = quantity;
}

function closeEditModal() {
    document.getElementById('edit-modal').style.display = 'none';
}

function openAddModal() {
    document.getElementById('add-item-modal').style.display = 'block';
}

function closeAddModal() {
    document.getElementById('add-item-modal').style.display = 'none';
}
