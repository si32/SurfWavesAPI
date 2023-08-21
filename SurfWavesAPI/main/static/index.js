// util function for csrf token
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

document.addEventListener("DOMContentLoaded", function () {
  let collect_btn = document.querySelector("#collect_btn_id");

  collect_btn.addEventListener("click", (e) => {
    console.log("started");
    // Чтобы не перезагружалась страница при отправки формы
    e.preventDefault();

    url = document.querySelector("#input_url_id").value;
    console.log(url);
    let csrftoken = getCookie("csrftoken");
    console.log(csrftoken);
    fetch("/api/crawl", {
      method: "POST",
      headers: { "X-CSRFToken": csrftoken },
      mode: "same-origin",
      body: JSON.stringify({
        url: url,
      }),
    })
      .then((result) => result.json())
      .then((data) => {
        console.log(data);
        let data_string = JSON.stringify(data);
        let output = document.querySelector("#output_id");
        output.innerHTML = `${data_string}`;
        if (data.status == "started") {
          let task_id = data.task_id;
          let unique_id = data.unique_id;
          statusInterval = setInterval(function () {
            check_status(task_id, unique_id);
          }, 2000);
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
});

function check_status(task_id, unique_id) {
  fetch(`/api/crawl/?task_id=${task_id}&unique_id=${unique_id}`)
    .then((result) => result.json())
    .then((data) => {
      let data_string = JSON.stringify(data);
      let output = document.querySelector("#output_id");
      output.innerHTML = `${data_string}`;
      if (!data.status) {
        clearInterval(statusInterval);
        console.log("finished!");
      }
    });
}
