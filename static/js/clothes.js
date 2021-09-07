$(document).ready(function () {
    let initial_price = "$" + $('input[name="slider-price"]').val()
    $("#price").val(initial_price)

    $('input[name="slider-price"]').change(function () {
        let newPrice = "$" + $(this).val()
        $("#price").val(newPrice)
    })
})