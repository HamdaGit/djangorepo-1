// Sample product data (replace with your actual data)
const products = [
    { image: "images/tshirt1.jpg", name: "T-shirt", price: "Rs.2000" },
    { image: "images/tshirt2.jpg", name: "T-shirt", price: "Rs.2000" },
    { image: "images/tshirt3.jpg", name: "T-shirt", price: "Rs.2000" },
    { image: "images/tshirt4.jpg", name: "T-shirt", price: "Rs.2000" },
    { image: "images/tshirt5.jpg", name: "T-shirt", price: "Rs.2000" },
    { image: "images/tshirt6.jpg", name: "T-shirt", price: "Rs.2000" },
    { image: "images/tshirt7.png", name: "T-shirt", price: "Rs.2000" },
    { image: "images/tshirt8.png", name: "T-shirt", price: "Rs.2000" },
    { image: "images/hoodie1.jpg", name: "Hoodie", price: "Rs.3000" },
    { image: "images/hoodie2.png", name: "Hoodie", price: "Rs.3000" },
    { image: "images/hoodie3.png", name: "Hoodie", price: "Rs.3000" },
    { image: "images/hoodie4.png", name: "Hoodie", price: "Rs.3000" },
    { image: "images/hoodie5.png", name: "Hoodie", price: "Rs.3000" },
    { image: "images/scarf2.jpg.webp", name: "Scarf", price: "Rs.3500" },
    { image: "images/scarf1.jpg.webp", name: "Scarf", price: "Rs.3500" },
    { image: "images/scarf3.jpg.webp", name: "Scarf", price: "Rs.3500" },
    { image: "images/Stole.jpg.webp", name: "Scarf", price: "Rs.3800" },
    { image: "images/scarf5.jpg.webp", name: "Scarf", price: "Rs.3800" },
    { image: "images/scarf7.jpg.webp", name: "Scarf", price: "Rs.3500" },
    { image: "images/scarf8.jpg.webp", name: "Scarf", price: "Rs.3500" },
    { image: "images/scarf9.jpg.webp", name: "Scarf", price: "Rs.3500" },
    { image: "images/scarf10.jpg.webp", name: "Scarf", price: "Rs.3500" },
    { image: "images/scarf11.jpg.webp", name: "Scarf", price: "Rs.3500" },
    { image: "images/shirt1.jpg.webp", name: "Shirt", price: "Rs.2500" },
    { image: "images/shirt2.jpg.webp", name: "Shirt", price: "Rs.2500" },
    { image: "images/shirt3.jpg.webp", name: "Shirt", price: "Rs.3000" },
    { image: "images/shirt4.jpg.webp", name: "Shirt", price: "Rs.3000" },
    { image: "images/shirt5.jpg", name: "Shirt", price: "Rs.2500" },
    { image: "images/shirt6.jpg.webp", name: "Shirt", price: "Rs.2800" },
    { image: "images/shirt7.jpg.webp", name: "Shirt", price: "Rs.2800" },
    { image: "images/shirt8.jpg.webp", name: "Shirt", price: "Rs.3100" },
    { image: "images/denim1.png", name: "Denim", price: "Rs.4000" },
    { image: "images/denim2.png", name: "Denim", price: "Rs.4000" },
    { image: "images/denim3.png", name: "Denim", price: "Rs.4000" },
    { image: "images/denim4.png", name: "Denim", price: "Rs.4000" },
    { image: "images/denim5.png", name: "Denim", price: "Rs.4000" },
    // Add more product data here
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
}
else {
    console.error('Invalid Product Index:', selectedProductIndex);
}
