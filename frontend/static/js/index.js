const mercadoPagoPublicKey = document.getElementById("mercado-pago-public-key").value;
const mercadopago = new MercadoPago(mercadoPagoPublicKey);
let cardPaymentBrickController;

async function loadPaymentForm(type) {
    const productCost = document.getElementById('amount').value;
    const settings = {
        initialization: {
            amount: productCost,
        },
        callbacks: {
            onReady: () => {
                console.log('brick ready')
            },
            onError: (error) => {
                alert(JSON.stringify(error))
            },
            onSubmit: (cardFormData) => {
                proccessPayment(cardFormData)
            }
        },
        locale: 'pt-BR',
        customization: {
            paymentMethods: {
                ticket: "all",
                bankTransfer: "all",
                creditCard: "all",
            },
            visual: {
                style: {
                    theme: 'dark',
                    customVariables: {
                        formBackgroundColor: 'maroon',
                        baseColor: '#fff'
                    }
                }
            }
        },
    }

    const bricks = mercadopago.bricks();
    cardPaymentBrickController = await bricks.create("payment", 'mercadopago-bricks-contaner__PaymentCard', settings);
};

const proccessPayment = (cardFormData) => {
    fetch("/process_payment", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(cardFormData),
    })
        .then(response => {
            return response.json();
        })
        .then(result => {
            if (!result.hasOwnProperty("error_message")) {
                document.getElementById("payment-id").innerText = result.id;
                document.getElementById("payment-status").innerText = result.status;
                if (result?.transaction_details?.external_resource_url) {
                    window.location.replace(result?.transaction_details?.external_resource_url);
                    redirect.style.display = 'block'
                    let redirect = document.getElementById('redirectmsg')
                }
                if (result?.point_of_interaction?.transaction_data?.qr_code_base64) {
                    const qrcode = document.getElementById("qrcode-pix")
                    const pixkeyout = document.getElementById("pix-key-outside")
                    const pixkey = document.getElementById('pix-key')
                    qrcode.src = "data:image/png;base64," + result?.point_of_interaction?.transaction_data?.qr_code_base64;
                    qrcode.style.display = "block"
                    pixkey.innerHTML = result?.point_of_interaction?.transaction_data?.qr_code
                    pixkey.style.display = 'block'
                    pixkeyout.style.display = 'block'
                    const copy = document.getElementById('copy')
                    copy.addEventListener('click',()=>{
                        navigator.clipboard.writeText(pixkey.innerText)
                    })
                    copy.style.display = 'block'
                }
                $('.container__payment').fadeOut(500);
                setTimeout(() => { $('.container__result').show(500).fadeIn(); }, 500);
            } else {
                alert(JSON.stringify({
                    status: result.status,
                    message: result.error_message
                }))
            }
        })
        .catch(error => {
            alert("Unexpected error\n" + JSON.stringify(error));
        });
}

// Handle transitions
document.getElementById('checkout-btn').addEventListener('click', function () {
    $('.container__cart').fadeOut(500);
    setTimeout(() => {
        loadPaymentForm('pix');
        $('.container__payment').show(500).fadeIn();
    }, 500);
});

document.getElementById('go-back').addEventListener('click', function () {
    $('.container__payment').fadeOut(500);
    setTimeout(() => { $('.container__cart').show(500).fadeIn(); }, 500);
});

// Handle price update
function updatePrice() {
    let unitPrice = document.getElementById('unit-price').innerText;

    document.getElementById('cart-total').innerText = '$ ' + unitPrice;
    document.getElementById('summary-price').innerText = '$ ' + unitPrice;
    document.getElementById('summary-total').innerText = '$ ' + unitPrice;
    document.getElementById('amount').value = unitPrice;
};



// document.getElementById('quantity').addEventListener('change', updatePrice);
updatePrice();