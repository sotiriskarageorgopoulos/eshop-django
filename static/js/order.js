$(document).ready(function () {
    let clothes = JSON.parse(localStorage.getItem('clothes'))
    clothes.map(c => {
        $("#productList").append(`
        <li class="list-group-item order-box">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-sm-6">
                        <p class="shopping-cart-brand">${c.brand}</p>
                        <p>Size: ${c.size}</p>
                        <p>Color: ${c.color}</p>
                        <p>Price: &dollar;${c.price}</p>
                        <p>Pieces: ${c.pieces}</p>
                    </div>
                    <div class="col-sm-6">
                    <img src="${c.image}" alt="${c.brand}" class="img-fluid" />
                    </div>
                </div>
            </div>
        </li> 
        `)
        $("#hiddenInputsCode").append(`
            <input type="hidden" name="code" value="${c.code}"/>
            <input type="hidden" name="${c.code}" value="${c.pieces}"/>
        `)
    })

    let totalCost = localStorage.getItem('totalCost')
    let shippingCost = localStorage.getItem('shippingCost')
    let existsTotalCost = totalCost !== undefined && totalCost !== null 
                      && shippingCost !== undefined && shippingCost !== null

    if(existsTotalCost) {
        $("#costBox").append(`
        <div class="container-fluid order-box mt-3 mb-3">
            <h2 class="order-heading">The cost</h2>
            <div class="row">
                <div class="col-sm">
                    <p class="order-cost-info">Real cost: &dollar;${totalCost - shippingCost}</p>
                    <p class="order-cost-info">Shipping cost: &dollar;${shippingCost}</p>
                    <p class="order-cost-info">Total cost: &dollar;${totalCost}</p>
                </div>
            </div>
        </div>
        `)
        $("#hiddenInputsCode").append(`
        <input type="hidden" name="total_cost" value="${totalCost}"/>
        `)
    }

    $("#payment_method").change(function () {
        let value = $(this).val()

        if(value === 'credit_card') {
            $("#hiddenInputsCC").append(`
            <label class="label-form" for="ccn">Credit Card Number</label>
            <input type="text" name="ccn" class="form-control order-form-input" id="ccn" maxlength="16" />
            <label class="label-form" for="ccv">CCV</label>
            <input type="text" name="ccv" class="form-control order-form-input" id="ccv" maxlength="3"/>
            `)
        }
        else {
            $("#hiddenInputs").empty() 
        }
        //ΦΤΙΑΧΝΩ RESPONSIVE
    })

    $("#order_btn").click(function () {
        localStorage.clear()
    })
})

