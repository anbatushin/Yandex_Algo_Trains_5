<div class="problem-statement">
   <div class="header">
      <h1 class="title">G. Построить квадрат</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>2&nbsp;секунды</td>
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
         <p>Задано множество, состоящее из <span class="tex-math-text">N</span> различных точек на плоскости. Координаты всех точек&nbsp;&mdash; целые числа. Определите, какое минимальное количество точек нужно добавить во множество, чтобы нашлось четыре точки, лежащие
            в вершинах квадрата.
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>В первой строке вводится число <span class="tex-math-text">N</span> (<span class="tex-math-text">1 &le; N &le; 2000</span>)&nbsp;&mdash; количество точек.
         </p></span><p>В следующих <span class="tex-math-text">N</span> строках вводится по два числа <span class="tex-math-text">x<sub>i</sub></span>, <span class="tex-math-text">y<sub>i</sub></span> (<span class="tex-math-text">-10<sup>8</sup> &le; x<sub>i</sub>, y<sub>i</sub> &le; 10<sup>8</sup></span>)&nbsp;&mdash; координаты точек.
      </p>
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>В первой строке выведите число <span class="tex-math-text">K</span>&nbsp;&mdash; минимальное количество точек, которые нужно добавить во множество.
         </p></span><p>В следующих <span class="tex-math-text">K</span> строках выведите координаты добавленных точек <span class="tex-math-text">x<sub>i</sub></span>, <span class="tex-math-text">y<sub>i</sub></span> через пробел. Координаты должны быть целыми и не превышать <span class="tex-math-text">10<sup>9</sup></span> по модулю.
      </p>
      <p>Если решений несколько&nbsp;&mdash; выведите любое из них.</p>
   </div>
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
0 1
1 0
</pre></td>
            <td><pre>2
0 0
1 1
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
0 2
2 0
2 2
</pre></td>
            <td><pre>1
0 0
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
            <td><pre>4
-1 1
1 1
-1 -1
1 -1
</pre></td>
            <td><pre>0  
</pre></td>
         </tr>
      </tbody>
   </table>