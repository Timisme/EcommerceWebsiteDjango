// 1. 按下 apply 按鈕，得到 input 的 code，並在後端認證
// 2. 如果驗證成功，並且該 coupon 是對運費有折扣，則呼叫 api 更新該筆訂單的運費。

const couponBtn = document.querySelector(".coupon-btn");
const couponInput = document.querySelector(".coupon-input");

if (couponBtn) {
  couponBtn.addEventListener("click", async function (e) {
    e.preventDefault();
    let code = couponInput.value;
    let url = "/coupon/";
    let data = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken
      },
      body: JSON.stringify({
        code: code
      })
    })
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        return data;
      });

    if (data["discount_type"] === "shipping") {
      await updateOrderShipping(data["discount"]);
      location.reload();
    }
  });
}

async function updateOrderShipping(value) {
  let currentOrderId = await getCurrentOrderId();
  let url = `/api/order/${currentOrderId}`;

  await fetch(url, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken
    },
    body: JSON.stringify({
      shipping_fee: value
    })
  })
    .then((res) => {
      return res.json();
    })
    .then((data) => {
      console.log("data after update shipping:", data);
    });
}
