<div class="problem-statement">
   <div class="header">
      <h1 class="title">G. Разрушить казарму</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>1&nbsp;секунда</td>
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
         <p>Вы играете в интересную стратегию. У вашего соперника остались всего одна казарма&nbsp;&mdash; здание, в котором постоянно появляются новые солдаты. Перед атакой у вас есть <span class="tex-math-text">x</span> солдат. За один раунд каждый солдат может убить одного из солдат противника или нанести 1 очко урона казарме (вычесть единицу
            здоровья у казармы). Изначально у вашего оппонента нет солдат. Тем не менее, его казарма имеет <span class="tex-math-text">y</span> единиц здоровья и производит <span class="tex-math-text">p</span> солдат за раунд.
         </p></span><p>Ход одного раунда: 
         <ol>
            <li>Каждый солдат из вашей армии либо убивает одного из солдат вашего противника, либо наносит 1 очко урона казарме. Каждый солдат
               может выбрать своё действие. Когда казарма теряет все свои единицы здоровья, она разрушается. 
            </li>
            <li>Ваш противник атакует. Он убьет <span class="tex-math-text">k</span> ваших солдат, где <span class="tex-math-text">k</span>&nbsp;&mdash; количество оставшихся у противника солдат. 
            </li>
            <li>Если казармы еще не разрушены, ваш противник производит <span class="tex-math-text">p</span> новых солдат. 
            </li>
         </ol>
      </p>
      <p>Ваша задача&nbsp;&mdash; разрушить казарму и убить всех солдат противника. Если это возможно, посчитайте минимальное количество раундов, которое вам
         нужно для этого. В противном случае выведите <span class="tex-math-text">-1</span>.
      </p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>На вход подаётся три целых числа <span class="tex-math-text">x</span>, <span class="tex-math-text">y</span>, <span class="tex-math-text">p</span> (<span class="tex-math-text">1 &le; x, y, p &le; 5000</span>)&nbsp;&mdash; количество ваших солдат на старте игры, количество очков здоровья казармы и количество производимых за раунд казармой солдат,
            соответственно. Каждое число расположено в новой строке.
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Если возможно убить всех вражеских солдат и разрушить казарму, выведите минимальное количество раундов, необходимых для этого.
            В противном случае выведите <span class="tex-math-text">-1</span>.
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
            <td><pre>10
11
15
</pre></td>
            <td><pre>4
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
            <td><pre>1
2
1
</pre></td>
            <td><pre>-1
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
            <td><pre>1
1
1
</pre></td>
            <td><pre>1
</pre></td>
         </tr>
      </tbody>
   </table>
   <h3>Пример 4</h3>
   <table class="sample-tests">
      <thead>
         <tr>
            <th>Ввод</th>
            <th>Вывод</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td><pre>25
200
10
</pre></td>
            <td><pre>13
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"><span style="">
         <p>В первом примере в первом раунде сначала все ваши солдату атакуют казарму, после этого не происходит ничего, потому что у
            врага нет солдат, затем у врага появляется <span class="tex-math-text">15</span> солдат. Во втором раунде один ваш солдат добивает казарму, остальные <span class="tex-math-text">9</span> солдат убивают <span class="tex-math-text">9</span> солдат врага. Оставшиеся <span class="tex-math-text">6</span> солдат врага убивают <span class="tex-math-text">6</span> ваших солдат, но армия врага не пополняется, поскольку казарма разрушена. В третьем раунде сначала вы убиваете четверых солдат
            врага, затем враг двоих ваших солдат. В последнем, четвертом, раунде вы добиваете двух оставшихся солдат врага.
         </p></span></div>