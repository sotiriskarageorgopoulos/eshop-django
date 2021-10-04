function removeProduct(code) {
    let clothes = JSON.parse(localStorage.getItem('clothes'))
    clothes = clothes.filter(c => c.code !== code)
    localStorage.setItem('clothes', JSON.stringify(clothes))
    calculateTotalCost()
    setTimeout(() => location.reload(), 1000)
}

function calculateTotalCost() {
    let clothes = JSON.parse(localStorage.getItem('clothes'))
    let totalCost = 0
    let realCost = 0
    let shippingCost = 0
    clothes.map(c => {
        if (c.pieces !== undefined) {
            realCost += Number(c.pieces) * Number(c.price)
            shippingCost = Number(c.shippingCost)
        } else {
            realCost += Number(c.price)
            shippingCost = Number(c.shippingCost)
        }
    })

    if (realCost > 50) {
        totalCost = realCost
        shippingCost = 0
    } else {
        totalCost = realCost + shippingCost
    }

    localStorage.setItem('totalCost', totalCost)
    localStorage.setItem('shippingCost', shippingCost)
}

$(document).ready(function () {
    $("#shopping-cart").on({
        mouseenter: createShoppingCart,
        click: function () {
            $("#show-shopping-cart").empty()
        }
    })
    $("#shopping-cart").on("taphold", createShoppingCart)

    function createShoppingCart() {
        let clothes = JSON.parse(localStorage.getItem('clothes'))
        let cartDetails = ``
        if (clothes !== null && clothes.length > 0) {
            clothes.map(c => {
                if (c.pieces !== undefined) {
                    cartDetails += `
                    <div class="container-fluid shopping-cart-details">
                        <div class="row">
                            <div class="col-sm-6">
                                <p class="shopping-cart-brand">${c.brand}</p>
                                <p>Size: ${c.size}</p>
                                <p>Color: ${c.color}</p>
                                <p>Price: &dollar;${c.price}</p>
                                <p>Pieces: ${c.pieces}</p>
                                <button class="btn remove-product-btn" onclick="removeProduct('${c.code}')">Remove</button>
                            </div>
                            <div class="col-sm-6">
                               <img src="${c.image}" alt="${c.brand}" class="img-fluid" />
                            </div>
                        </div>
                    </div>
                    `
                } else {
                    cartDetails += `
                    <div class="container-fluid shopping-cart-details">
                        <div class="row">
                            <div class="col-sm-6">
                                <p class="shopping-cart-brand">${c.brand}</p>
                                <p>Size: ${c.size}</p>
                                <p>Color: ${c.color}</p>
                                <p>Price: &dollar;${c.price}</p>
                                <button class="btn remove-product-btn" onclick="removeProduct('${c.code}')">Remove</button>
                            </div>
                            <div class="col-sm-6">
                               <img src="${c.image}" alt="${c.brand}" class="img-fluid" />
                            </div>
                        </div>
                    </div>
                    `
                }
            })
        } else {
            cartDetails = `<p class="d-flex justify-content-center">Add Something...</p>`
        }

        let totalCost = localStorage.getItem('totalCost')
        let shippingCost = localStorage.getItem('shippingCost')
        let totalCostDetails = ``
        if (totalCost !== null && clothes.length > 0 && shippingCost <= 0) {
            totalCostDetails = `
            <p class="mt-3 shopping-cart-cost"><i class="bi bi-cart"></i> Total cost: &dollar;${totalCost}</p>
            <p class="mt-3 shopping-cart-cost">No shipping cost!</p>
            <a class="btn sc-order-btn" href="order">Order</a>
            `
        } else if (totalCost !== null && clothes.length > 0 && shippingCost > 0) {
            totalCostDetails = `
            <p class="mt-3 shopping-cart-cost"><i class="bi bi-cart"></i> Total cost: &dollar;${totalCost}</p>
            <p class="mt-2 shopping-cart-cost">Shipping Cost: &dollar;${shippingCost}</p>
            <a class="btn sc-order-btn" href="order">Order</a>
            `
        }

        $("#show-shopping-cart").append(`
        <div class="container-fluid shopping-cart">
            <div class="row">
                <h2 class="d-flex justify-content-center">My shopping cart</h2>
                <div class="col-sm">
                    <div class="">
                        ${cartDetails}
                    </div> 
                </div>
                ${totalCostDetails}
            </div>
        </div>
        `)
    }
})