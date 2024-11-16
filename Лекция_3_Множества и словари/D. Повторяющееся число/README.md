<div class="problem-statement">
   <div class="header">
      <h1 class="title">D. Повторяющееся число</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>1&nbsp;секунда</td>
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
         <p>Вам дана последовательность измерений некоторой величины. Требуется определить, повторялась ли какое-либо число, причём расстояние
            между повторами не превосходило <span class="tex-math-text">k</span>.
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке задаются два числа <span class="tex-math-text">n</span> и <span class="tex-math-text">k</span> (<span class="tex-math-text">1 &le; n, k &le; 10<sup>5</sup></span>).
         </p></span><p>Во второй строке задаются <span class="tex-math-text">n</span> чисел, по модулю не превосходящих <span class="tex-math-text">10<sup>9</sup></span>.
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите YES, если найдется повторяющееся число и расстояние между повторами не превосходит <span class="tex-math-text">k</span> и NO в противном случае.
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
            <td><pre>4 2
1 2 3 1
</pre></td>
            <td><pre>NO
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
            <td><pre>4 1
1 0 1 1</pre></td>
            <td><pre>YES
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
            <td><pre>6 2
1 2 3 1 2 3</pre></td>
            <td><pre>NO
</pre></td>
         </tr>
      </tbody>
   </table>
</div>