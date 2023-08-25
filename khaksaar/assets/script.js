
const products = [
    { image: "{% static 'tshirt1.jpg' %}", name: "T-shirt", price: "Rs.2000" },
    { image: "{% static 'tshirt2.jpg' %}", name: "T-shirt", price: "Rs.2000" },
    { image: "{% static 'tshirt3.jpg' %}", name: "T-shirt", price: "Rs.2000" },
    { image: "{% static 'tshirt4.jpg' %}", name: "T-shirt", price: "Rs.2000" },
    { image: "{% static 'tshirt5.jpg' %}", name: "T-shirt", price: "Rs.2000" },
    { image: "{% static 'tshirt6.jpg' %}", name: "T-shirt", price: "Rs.2000" },
    { image: "{% static 'tshirt7.png' %}", name: "T-shirt", price: "Rs.2000" },
    { image: "{% static 'tshirt8.png' %}", name: "T-shirt", price: "Rs.2000" },
    { image: "{% static 'hoodie1.jpg' %}", name: "Hoodie", price: "Rs.3000" },
    { image: "{% static 'hoodie2.png' %}", name: "Hoodie", price: "Rs.3000" },
    { image: "{% static 'hoodie3.png' %}", name: "Hoodie", price: "Rs.3000" },
    { image: "{% static 'hoodie4.png' %}", name: "Hoodie", price: "Rs.3000" },
    { image: "{% static 'hoodie5.png' %}", name: "Hoodie", price: "Rs.3000" },
    { image: "{% static 'scarf2.jpg.webp' %}", name: "Scarf", price: "Rs.3500" },
    { image: "{% static 'scarf1.jpg.webp' %}", name: "Scarf", price: "Rs.3500" },
    { image: "{% static 'scarf3.jpg.webp' %}", name: "Scarf", price: "Rs.3500" },
    { image: "{% static 'Stole.jpg.webp' %}", name: "Scarf", price: "Rs.3800" },
    { image: "{% static 'scarf5.jpg.webp' %}", name: "Scarf", price: "Rs.3800" },
    { image: "{% static 'scarf7.jpg.webp' %}", name: "Scarf", price: "Rs.3500" },
    { image: "{% static 'scarf8.jpg.webp' %}", name: "Scarf", price: "Rs.3500" },
    { image: "{% static 'scarf9.jpg.webp' %}", name: "Scarf", price: "Rs.3500" },
    { image: "{% static 'scarf10.jpg.webp' %}", name: "Scarf", price: "Rs.3500" },
    { image: "{% static 'scarf11.jpg.webp' %}", name: "Scarf", price: "Rs.3500" },
    { image: "{% static 'shirt1.jpg.webp' %}", name: "Shirt", price: "Rs.2500" },
    { image: "{% static 'shirt2.jpg.webp' %}", name: "Shirt", price: "Rs.2500" },
    { image: "{% static 'shirt3.jpg.webp' %}", name: "Shirt", price: "Rs.3000" },
    { image: "{% static 'shirt4.jpg.webp' %}", name: "Shirt", price: "Rs.3000" },
    { image: "{% static 'shirt5.jpg' %}", name: "Shirt", price: "Rs.2500" },
    { image: "{% static 'shirt6.jpg.webp' %}", name: "Shirt", price: "Rs.2800" },
    { image: "{% static 'shirt7.jpg.webp' %}", name: "Shirt", price: "Rs.2800" },
    { image: "{% static 'shirt8.jpg.webp' %}", name: "Shirt", price: "Rs.3100" },
    { image: "{% static 'denim1.png' %}", name: "Denim", price: "Rs.4000" },
    { image: "{% static 'denim2.png' %}", name: "Denim", price: "Rs.4000" },
    { image: "{% static 'denim3.png' %}", name: "Denim", price: "Rs.4000" },
    { image: "{% static 'denim4.png' %}", name: "Denim", price: "Rs.4000" },
    { image: "{% static 'denim5.png' %}", name: "Denim", price: "Rs.4000" },
    
];


// Get the index of the selected product from query parameter
const urlParams = new URLSearchParams(window.location.search);
const selectedProductIndex = parseInt(urlParams.get('productIndex'));
// Log the products array and the query parameter
console.log('Products Array:', products);
console.log('Selected Product Index:', selectedProductIndex);



// Update the product detail page with the selected product's data
if (!isNaN(selectedProductIndex) && selectedProductIndex >= 0 && selectedProductIndex < products.length) {
    const selectedProduct = products[selectedProductIndex];
    document.getElementById('productImage').src = selectedProduct.image;
    document.getElementById('productName').textContent = selectedProduct.name;
    document.getElementById('productPrice').textContent = selectedProduct.price;

    console.log('Product details updated:', selectedProduct);

}

