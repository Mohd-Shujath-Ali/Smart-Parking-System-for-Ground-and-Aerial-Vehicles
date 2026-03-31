<!DOCTYPE html>
<html>

<head>
  <title>Parking Dashboard</title>
</head>

<body>

  <h1>Slot Status: <span id="status">Loading...</span></h1>

  <button onclick="book()">Book Slot</button>
  <button onclick="cancel()">Cancel</button>

  <script type="module">
    import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-app.js";
    import { getDatabase, ref, onValue, runTransaction } from "https://www.gstatic.com/firebasejs/10.7.0/firebase-database.js";

    const app = initializeApp({
      databaseURL: "Your_Firebase_Database_URL"
    });

    const db = getDatabase(app);

  
    const slotRef = ref(db, "parking/slot1");

    let currentData = null;

    onValue(slotRef, (snap) => {
      const data = snap.val();

      if (!data) return;

      document.getElementById("status").innerText = data.status;
    });


    window.book = function () {
      runTransaction(slotRef, (data) => {
        if (!data) return;

        if (data.emergency == 1) {
          alert("🚨 Emergency! Cannot book");
          return;
        }


        if (data.final == 1) {
          alert("Slot occupied!");
          return;
        }

        if (data.booked == 1) {
          alert("Already booked!");
          return;
        }

        data.booked = 1;
        data.status = "booked";

        return data;
      });
    };

   
    window.cancel = function () {
      runTransaction(slotRef, (data) => {
        if (!data) return;

        if (data.emergency == 1) {
          alert("🚨 Emergency! Cannot cancel");
          return;
        }

        if (data.booked != 1) {
          alert("You can only cancel if booked!");
          return;
        }

        data.booked = 0;
        data.status = "available";

        return data;
      });
    };
  </script>

</body>

</html>
