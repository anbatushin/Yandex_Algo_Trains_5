<div class="problem-statement">
   <div class="header">
      <h1 class="title">H. Наилучший запрет</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>3&nbsp;секунды</td>
         </tr>
         <tr class="memory-limit">
            <td class="property-title">Ограничение памяти</td>
            <td>256Mb</td>
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
         <p>Константин и Михаил играют в настольную игру &laquo;Ярость Эльфов&raquo;. В игре есть <span class="tex-math-text">n</span> рас и <span class="tex-math-text">m</span> классов персонажей. Каждый персонаж характеризуется своими расой и классом. Для каждой расы и каждого класса существует ровно
            один персонаж такой расы и такого класса. Сила персонажа <span class="tex-math-text">i</span>-й расы и <span class="tex-math-text">j</span>-го класса равна <span class="tex-math-text">a<sub>i j</sub></span>, и обоим игрокам это прекрасно известно.
         </p></span><p>Сейчас Константин будет выбирать себе персонажа. Перед этим Михаил может запретить одну расу <span style="font-weight:bold;">и</span> один класс, чтобы Константин не мог выбирать персонажей, у которых такая раса <span style="font-weight:bold;">или</span> такой класс. Конечно же, Михаил старается, чтобы Константину достался как можно более слабый персонаж, а Константин, напротив,
         выбирает персонажа посильнее. Какие расу и класс следует запретить Михаилу?
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Первая строка содержит два целых числа <span class="tex-math-text">n</span> и <span class="tex-math-text">m</span> (<span class="tex-math-text">2 &le; n,m &le; 1000</span>) через пробел&nbsp;&mdash; количество рас и классов в игре &laquo;Ярость Эльфов&raquo;, соответственно.
         </p></span><p>В следующих <span class="tex-math-text">n</span> строках содержится по <span class="tex-math-text">m</span> целых чисел через пробел. <span class="tex-math-text">j</span>-е число <span class="tex-math-text">i</span>-й из этих строк&nbsp;&mdash; это <span class="tex-math-text">a<sub>i j</sub></span> (<span class="tex-math-text">1 &le; a<sub>i j</sub> &le; 10<sup>9</sup></span>).
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>В единственной строке выведите два целых числа через пробел&nbsp;&mdash; номер расы и номер класса, которые следует запретить Михаилу. Расы и классы нумеруются с единицы. Если есть несколько возможных
            ответов, выведите любой из них.
         </p></span></div>
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
            <td><pre>2 2
1 2
3 4
</pre></td>
            <td><pre>2 2
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
            <td><pre>3 4
1 3 5 7
9 11 2 4
6 8 10 12
</pre></td>
            <td><pre>3 2
</pre></td>
         </tr>
      </tbody>
   </table>
</div>