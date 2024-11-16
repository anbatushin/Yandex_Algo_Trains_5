<div class="problem-statement">
   <div class="header">
      <h1 class="title">A. Минимальный прямоугольник</h1>
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
         <p>На клетчатой плоскости закрашено K клеток. Требуется найти минимальный по площади прямоугольник, со сторонами, параллельными
            линиям сетки, покрывающий все закрашенные клетки.
         </p></span></div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Во входном файле, на первой строке, находится число <span class="tex-math-text">K</span> (<span class="tex-math-text">1 &le; K &le; 100</span>). На следующих <span class="tex-math-text">K</span> строках находятся пары чисел <span class="tex-math-text">X<sub>i</sub></span> и <span class="tex-math-text">Y<sub>i</sub></span>&nbsp;&mdash; координаты закрашенных клеток (<span class="tex-math-text">|X<sub>i</sub>|</span>, <span class="tex-math-text">|Y<sub>i</sub>| &le; 10<sup>9</sup></span>).
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите в выходной файл координаты левого нижнего и правого верхнего углов прямоугольника.</p></span></div>
   <h2>Пример</h2>
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
1 3
3 1
3 5
6 3
</pre></td>
            <td><pre>1 1 6 5</pre></td>
         </tr>
      </tbody>
   </table>
</div>