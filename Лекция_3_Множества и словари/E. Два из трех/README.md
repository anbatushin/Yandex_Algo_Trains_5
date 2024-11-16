<div class="problem-statement">
   <div class="header">
      <h1 class="title">E. Два из трех</h1>
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
         <p>Вам даны три списка чисел. Найдите все числа, которые встречаются хотя бы в двух из трёх списков.</p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Во входных данных описывается три списка чисел. Первая строка каждого описания списка состоит из длины списка <span class="tex-math-text">n</span> (<span class="tex-math-text">1 &le; n &le; 1000</span>). Вторая строка описания содержит список натуральных чисел, записанных через пробел. Числа не превосходят <span class="tex-math-text">10<sup>9</sup></span>.
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите все числа, которые содержатся хотя бы в двух списках из трёх, в порядке возрастания. Обратите внимание, что каждое
            число необходимо выводить только один раз.
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
            <td><pre>2
3 1
2
1 3
2
1 2
</pre></td>
            <td><pre>1 3
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
            <td><pre>3
1 2 2
3
3 4 3
1
5</pre></td>
            <td><pre>
</pre></td>
         </tr>
      </tbody>
   </table>