$(document).ready(function () {
    $("#shopping-cart").on({
        mouseenter: function () {
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
                                    <p>Shipping Cost: &dollar;${c.shippingCost}</p>
                                    <input type="hidden" name="cloth_code" value="${c.code}"/>
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
                                    <p>Shipping Cost: &dollar;${c.shippingCost}</p>
                                    <input type="hidden" name="cloth_code" value="${c.code}"/>
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
            let totalCostDetails = ``
            if (totalCost !== null && clothes.length > 0) {
                totalCostDetails = `
                <p class="mt-3 shopping-cart-cost"><i class="bi bi-cart"></i> Total cost: &dollar;${totalCost}</p>
                <button class="btn sc-order-btn">Order</button>
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
        },
        click: function () {
            $("#show-shopping-cart").empty()
        }
    })
})