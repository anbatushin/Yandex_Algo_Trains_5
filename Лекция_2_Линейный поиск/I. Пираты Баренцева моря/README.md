<div class="problem-statement">
   <div class="header">
      <h1 class="title">I. Пираты Баренцева моря</h1>
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
   <div class="legend"> Вася играет в настольную игру «Пираты Баренцева моря», которая посвящена морским битвам. Игровое поле представляет собой
      квадрат из <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi>
      <mo>×</mo> <mi>N</mi></math> клеток, на котором расположено <!--l. 47--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math>
      кораблей (каждый корабль занимает одну клетку). <!--l. 49-->
      <p style="text-indent: 0em;">Вася решил воспользоваться линейной тактикой, для этого ему необходимо выстроить все <!--l. 49--><math
      display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math> кораблей в одном столбце.
      За один ход можно передвинуть один корабль в одну из четырёх соседних по стороне клеток. Номер столбца, в котором будут выстроены
      корабли, не важен. Определите минимальное количество ходов, необходимых для построения кораблей в одном столбце. В начале
      и процессе игры никакие два корабля не могут находиться в одной клетке. </p>
      
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"> В первой строке входных данных задаётся число <!--l. 52--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math>
      (<!--l. 52--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn> <mo>≤</mo>
      <mi>N</mi> <mo>≤</mo> <mn>1</mn><mn>0</mn><mn>0</mn></math>). <!--l. 54-->
      <p style="text-indent: 0em;">В каждой из следующих <!--l. 54--><math display="inline" style="text-indent: 0em;" xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math>
      строк задаются координаты корабля: сначала номер строки, затем номер столбца (нумерация начинается с единицы). </p>
      
   </div>
   <h2>Формат вывода</h2>
   <div class="output-specification"> Выведите одно число&nbsp;— минимальное количество ходов, необходимое для построения. </div>
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
            <td><pre>3
1 2
3 3
1 1
</pre></td>
            <td><pre>3
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"> В примере необходимо выстроить корабли в столбце номер 2. Для этого необходимо переставить корабль из клетки 3 3 в клетку
      3 2 за один ход, а корабль из клетки 1 1 в клетку 2 2 за два хода. Существуют и другие варианты перестановки кораблей, однако
      ни в одном из них нет меньше трёх ходов. 
   </div>