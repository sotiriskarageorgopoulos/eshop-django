$(document).ready(function () {
    $("#shopping-cart").on({
        mouseenter: function () {
            $("#show-shopping-cart").append(`
            <div class="shopping-cart-triangle"></div>
            <div class="container-fluid shopping-cart">
                <div class="row">
                    <h2 class="d-flex justify-content-center">My shopping cart</h2>
                    <div class="col-sm shopping-cart-details">
                        <p>Product 1: &dollar;20</p>
                        <p>Product 1: &dollar;20</p>
                        <p><i class="bi bi-cart"></i> Total cost: &dollar;40</p>
                    </div>
                </div>
            </div>
            `)
        },
        mouseleave: function () {
            $("#show-shopping-cart").empty()
        }
    })
})