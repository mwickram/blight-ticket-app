function onClickedSubmit(){
    console.log("Submit button");
    var fine_ = document.getElementById("uiFine");
    var discount_ = document.getElementById("uiDiscount");
    var jamount = document.getElementById("uiJamount");
    var late = document.getElementById("uiLate");
    var estProb = document.getElementById("uiProb");
    

    var url = "http://127.0.0.1:5000/predict_prob";

    $.post(url, {
        fine: parseFloat(fine_.value),
        discount: parseFloat(discount_.value),
        judgment_amount: parseFloat(jamount.value),
        late_fee: parseFloat(late.value)
    }, function(data, status){
        console.log(data.probability);
        estProb.innerHTML = "<h2>" + data.probability.toString() + "</h2>";
        console.log(status);
    });
}