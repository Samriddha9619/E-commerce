
let cart = JSON.parse(localStorage.getItem('cart') || '[]');

function addToCart(productId, productName, price, quantity = 1) {
    const existingItem = cart.find(item => item.id === productId);
    
    if (existingItem) {
        existingItem.quantity += parseInt(quantity);
    } else {
        cart.push({
            id: productId,
            name: productName,
            price: price,
            quantity: parseInt(quantity)
        });
    }
    
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
    
    alert('Product added to cart!');
}

function updateCartCount() {
    const cartCount = cart.reduce((total, item) => total + item.quantity, 0);
    document.getElementById('cart-count').textContent = cartCount;
}

document.addEventListener('DOMContentLoaded', function() {
    updateCartCount();
});

function validateForm(formId) {
    const form = document.getElementById(formId);
    const inputs = form.querySelectorAll('input[required], textarea[required]');
    
    for (let input of inputs) {
        if (!input.value.trim()) {
            alert(`Please fill in the ${input.labels[0].textContent} field.`);
            input.focus();
            return false;
        }
    }
    return true;
}