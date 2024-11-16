<div class="problem-statement">
   <div class="header">
      <h1 class="title">B. Футбольный комментатор</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>2&nbsp;секунды</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>64Mb</td>
         </tr>
         <tr class="input-file">
            <td class="property-title">Ввод</td>
            <td colspan="1">стандартный ввод или input.txt</td>
         </tr>
         <tr class="output-file">
            <td class="property-title">Вывод</td>
            <td colspan="1">стандартный вывод или output.txt</td>
         </tr>
      </table>
   </div>
   <h2></h2>
   <div class="legend"><span style="">
         <p>Раунд плей-офф между двумя командами состоит из двух матчей. Каждая команда проводит по одному матчу &laquo;дома&raquo; и &laquo;в гостях&raquo;. Выигрывает команда, забившая большее число мячей. Если же число забитых мячей совпадает, выигрывает команда, забившая больше
            мячей &laquo;в гостях&raquo;. Если и это число мячей совпадает, матч переходит в дополнительный тайм или серию пенальти.
         </p></span><p>Вам дан счёт первого матча, а также счёт текущей игры (которая ещё не завершилась). Помогите комментатору сообщить, сколько
         голов необходимо забить первой команде, чтобы победить, не переводя игру в дополнительное время.
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке записан счёт первого мачта в формате <span class="tex-math-text">G<sub>1</sub>:G<sub>2</sub></span>, где <span class="tex-math-text">G<sub>1</sub></span> &mdash; число мячей, забитых первой командой, а <span class="tex-math-text">G<sub>2</sub></span> &mdash; число мячей, забитых второй командой.
         </p></span><p>Во второй строке записан счёт второго (текущего) матча в аналогичном формате. Все числа в записи счёта не превышают <span class="tex-math-text">5</span>.
      </p>
      <p>В третьей строке записано число <span class="tex-math-text">1</span>, если первую игру первая команда провела &laquo;дома&raquo;, или <span class="tex-math-text">2</span>, если &laquo;в гостях&raquo;.
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите единственное целое число "&mdash; необходимое количество мячей.</p></span></div>
   <h3>Пример 1</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>0:0
0:0
1
</pre></td>
            <td><pre>1
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 2</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>0:2
0:3
1
</pre></td>
            <td><pre>5
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 3</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>0:2
0:3
2
</pre></td>
            <td><pre>6
</pre></td>