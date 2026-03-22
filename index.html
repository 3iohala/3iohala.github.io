<!DOCTYPE html>
<html lang="lt">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Snake Game</title>
  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background: #111;
      color: white;
      text-align: center;
    }

    h1 {
      margin-top: 20px;
    }

    p {
      margin: 6px 0;
    }

    canvas {
      background: black;
      display: block;
      margin: 20px auto;
      border: 2px solid white;
    }

    button {
      padding: 10px 18px;
      font-size: 16px;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      background: #2e8b57;
      color: white;
    }

    button:hover {
      background: #246b44;
    }
  </style>
</head>
<body>
  <h1>Snake Game</h1>
  <p>Valdymas: rodyklių klavišai</p>
  <p>Perkrauti: R</p>
  <p id="score">Taškai: 0</p>
  <canvas id="game" width="600" height="400"></canvas>
  <button onclick="restartGame()">Pradėti iš naujo</button>

  <script>
    // Pasiimame piešimo lauką (canvas)
    const canvas = document.getElementById("game");
    const ctx = canvas.getContext("2d");

    // Parodys taškus ekrane
    const scoreText = document.getElementById("score");

    // Vieno langelio dydis
    const cellSize = 20;

    // Kiek langelių telpa į plotį ir aukštį
    const cols = canvas.width / cellSize;
    const rows = canvas.height / cellSize;

    // Kintamieji žaidimui
    let snake;
    let direction;
    let food;
    let score;
    let gameOver;

    // Greitis milisekundėmis
    // Didesnis skaičius = lėtesnė gyvatė
    let speed = 200;

    // Šitas kintamasis padeda valdyti laiką
    let lastTime = 0;

    // Sukuriame pradinę žaidimo būseną
    function initGame() {
      // Gyvatė pradeda iš 3 dalių
      snake = [
        { x: 5, y: 5 },
        { x: 4, y: 5 },
        { x: 3, y: 5 }
      ];

      // Pradinė kryptis: į dešinę
      direction = { x: 1, y: 0 };

      // Taškai nuo 0
      score = 0;

      // Žaidimas dar nesibaigė
      gameOver = false;

      // Sukuriame maistą
      food = randomFood();

      // Atnaujiname tekstą
      scoreText.textContent = "Taškai: " + score;
    }

    // Ši funkcija suranda vietą maistui
    function randomFood() {
      while (true) {
        const newFood = {
          x: Math.floor(Math.random() * cols),
          y: Math.floor(Math.random() * rows)
        };

        // Tikriname, kad maistas neatsirastų ant gyvatės
        let onSnake = snake.some(segment => segment.x === newFood.x && segment.y === newFood.y);

        if (!onSnake) {
          return newFood;
        }
      }
    }

    // Nupiešia vieną langelį
    function drawCell(x, y, color) {
      ctx.fillStyle = color;
      ctx.fillRect(x * cellSize, y * cellSize, cellSize, cellSize);

      // Juodas rėmelis aplink langelį
      ctx.strokeStyle = "black";
      ctx.strokeRect(x * cellSize, y * cellSize, cellSize, cellSize);
    }

    // Nupiešia visą žaidimą
    function drawGame() {
      // Uždažome foną juodai
      ctx.fillStyle = "black";
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // Nupiešiame maistą
      drawCell(food.x, food.y, "red");

      // Nupiešiame gyvatę
      snake.forEach((segment, index) => {
        // Galva tamsesnė
        if (index === 0) {
          drawCell(segment.x, segment.y, "darkgreen");
        } else {
          drawCell(segment.x, segment.y, "limegreen");
        }
      });

      // Jei žaidimas baigėsi, parodome tekstą
      if (gameOver) {
        ctx.fillStyle = "white";
        ctx.font = "30px Arial";
        ctx.fillText("Game Over", canvas.width / 2 - 90, canvas.height / 2 - 10);
        ctx.font = "20px Arial";
        ctx.fillText("Spausk R, kad pradėtum iš naujo", canvas.width / 2 - 145, canvas.height / 2 + 30);
      }
    }

    // Pajudina gyvatę
    function updateGame() {
      if (gameOver) return;

      // Nauja galvos vieta
      const head = {
        x: snake[0].x + direction.x,
        y: snake[0].y + direction.y
      };

      // Tikriname, ar atsitrenkė į sieną
      if (
        head.x < 0 ||
        head.x >= cols ||
        head.y < 0 ||
        head.y >= rows
      ) {
        gameOver = true;
        return;
      }

      // Tikriname, ar atsitrenkė į save
      for (let segment of snake) {
        if (segment.x === head.x && segment.y === head.y) {
          gameOver = true;
          return;
        }
      }

      // Įdedame naują galvą į pradžią
      snake.unshift(head);

      // Jei suvalgė maistą
      if (head.x === food.x && head.y === food.y) {
        score++;
        scoreText.textContent = "Taškai: " + score;
        food = randomFood();
      } else {
        // Jei nesuvalgė, nuimame uodegą
        snake.pop();
      }
    }

    // Pagrindinis žaidimo ciklas
    function gameLoop(timestamp) {
      // Judiname tik kas tam tikrą laiką
      if (timestamp - lastTime > speed) {
        updateGame();
        drawGame();
        lastTime = timestamp;
      }

      requestAnimationFrame(gameLoop);
    }

    // Perkrauna žaidimą
    function restartGame() {
      initGame();
      drawGame();
    }

    // Valdymas klaviatūra
    document.addEventListener("keydown", (event) => {
      // Neleidžiame apsisukti tiesiai atgal
      if (event.key === "ArrowUp" && direction.y !== 1) {
        direction = { x: 0, y: -1 };
      } else if (event.key === "ArrowDown" && direction.y !== -1) {
        direction = { x: 0, y: 1 };
      } else if (event.key === "ArrowLeft" && direction.x !== 1) {
        direction = { x: -1, y: 0 };
      } else if (event.key === "ArrowRight" && direction.x !== -1) {
        direction = { x: 1, y: 0 };
      } else if (event.key === "r" || event.key === "R") {
        restartGame();
      }
    });

    // Paleidžiame žaidimą
    initGame();
    drawGame();
    requestAnimationFrame(gameLoop);
  </script>
</body>
</html>
