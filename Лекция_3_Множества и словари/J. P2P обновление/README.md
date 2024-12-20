<div class="problem-statement">
   <div class="header">
      <h1 class="title">J. P2P обновление</h1>
      <table>
         <tr class="time-limit">
            <td class="property-title">Ограничение времени</td>
            <td>15&nbsp;секунд</td>
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
         <p>В системе умного дома под управлением голосового помощника Лариса <span class="tex-math-text">n</span> устройств, соединяющихся между собой по сети LoRaWAN. Устройство номер 1 подключено к интернету и на него было скачано обновление,
            которое необходимо передать на все устройства.
         </p></span><p>Сеть LoRaWAN очень медленная, поэтому для распространения протокола был придуман peer-to-peer (P2P) протокол. Файл обновления
         разбивается на <span class="tex-math-text">k</span> одинаковых по размеру частей, занумерованных от 1 до <span class="tex-math-text">k</span>. 
      </p>
      <p>Передача части обновления происходит во время таймслотов. Каждый таймслот занимает одну минуту. За один таймслот каждое устройство
         может получить и передать ровно одну часть обновления. То есть устройство во время таймслота может получать новую часть обновления
         и передавать уже имеющуюуся у него к началу таймслота часть обновления, или совершать только одно из этих действий, или вообще
         не осуществлять прием или передачу. После приема части обновления устройство может передавать эту часть обновления другим
         устройствам в следующих таймслотах.
      </p>
      <p>Перед каждым таймслотом для каждой части обновления определяется, на скольких устройствах сети скачана эта часть. Каждое устройство
         выбирает отсутствующую на нем часть обновления, которая встречается в сети реже всего. Если таких частей несколько, то выбирается
         отсутствующая на устройстве часть обновления с наименьшим номером.
      </p>
      <p>После этого устройство делает запрос выбранной части обновления у одного из устройств, на котором такая часть обновления уже
         скачана. Если таких устройств несколько&nbsp;&mdash; выбирается устройство, на котором скачано наименьшее количество частей обновления. Если и таких устройств оказалось несколько&nbsp;&mdash; выбирается устройство с минимальным номером.
      </p>
      <p>После того, как все запросы отправлены, каждое устройство выбирает, чей запрос удовлетворить. Устройство <span class="tex-math-text">A</span> удовлетворяет тот запрос, который поступил от наиболее ценного для <span class="tex-math-text">A</span> устройства. Ценность устройства <span class="tex-math-text">B</span> для устройства <span class="tex-math-text">A</span> определяется как количество частей обновления, ранее полученных устройством <span class="tex-math-text">A</span> от устройства <span class="tex-math-text">B</span>. Если на устройство <span class="tex-math-text">A</span> пришло несколько запросов от одинаково ценных устройств, то удовлетворяется запрос того устройства, на котором меньше всего
         скачанных частей обновления. Если и таких запросов несколько, то среди них выбирается устройство с наименьшим номером.
      </p>
      <p>Далее начинается новый таймслот. Устройства, чьи запросы удовлетворены, скачивают запрошенную часть обновления, а остальные
         не скачивают ничего.
      </p>
      <p>Для каждого устройства определите, сколько таймслотов понадобится для скачивания всех частей обновления.</p>
   </div>
   <h2>Формат ввода</h2>
   <div class="input-specification"><span style="">
         <p>Вводится два числа <span class="tex-math-text">n</span> и <span class="tex-math-text">k</span> (<span class="tex-math-text">2 &le; n &le; 100</span>, <span class="tex-math-text">1 &le; k &le; 200</span>).
         </p></span></div>
   <h2>Формат вывода</h2>
   <div class="output-specification"><span style="">
         <p>Выведите <span class="tex-math-text">n-1</span> число&nbsp;&mdash; количество таймслотов, необходимых для скачивания обновления на устройства с номерами от 2 до <span class="tex-math-text">n</span>.
         </p></span></div>
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
            <td><pre>3 2
</pre></td>
            <td><pre>3 3
</pre></td>
         </tr>
      </tbody>
   </table>
   <h2>Примечания</h2>
   <div class="notes"><span style="">
         <p>Для удобства будем пользоваться обозначениями устройств буквами A, B, C (соответствует устройствам с номерами 1, 2 и 3). На
            устройстве A есть обе части обновления, а на устройствах B и C&nbsp;&mdash; ни одной.
         </p></span><p>Перед первым таймслотом для каждой части определяется количество устройств, на которых скачана каждая часть обновления: и
         1 и 2 часть обновления присутствуют только на одном устройстве.
      </p>
      <p>Устройства B и C выбирают самую редкую отсутствующую у них часть обновления с минимальным номером: самая редкая часть с минимальным
         номером&nbsp;&mdash; это часть 1. Она отсутствует и на устройстве B, и на устройстве С. Они запрашивают ее у устройства A. Ценность устройств
         B и C для устройства A равна нулю. Количество имеющихся у устройств B и C частей обновления одинакова и равно нулю. Поэтому
         устройство A выбирает устройство с минимальным номером (B). Во время первого таймслота выполняется передача части 1 с устройства
         A на устройство B. Ценность устройства A для устройства B становится равной 1.
      </p>
      <p>Перед вторым таймслотом для каждой части определяется количество устройств, на которых скачана каждая часть обновления: самой
         редкой оказывается часть 2 (присутствует только на устройстве A), следующая по редкости часть 1 (присутствует на устройствах
         A и B).
      </p>
      <p>Устройства B и C выбирают среди отсутствующих у них частей обновления самую редкую: для обоих устройств выбирается часть 2.
         Каждое из них делает запрос части 2 у единственного обладателя этой части&nbsp;&mdash; устройства A. Ценность устройств B и C для устройства A одинакова и равна нулю. Количество имеющихся у устройства C частей
         (0) меньше, чем у устройства B (1), поэтому выбирается устройство C. Во время второго таймслота выполняется передача части
         2 с устройства A на устройство C. Ценность устройства A для устройства C становится равной 1.
      </p>
      <p>Перед третьим таймслотом для каждой части определяется количество устройств, на которых скачана каждая часть обновления: обе
         части 1 и 2 присутствуют на двух устройствах (часть 1 на устройствах A и B, часть 2&nbsp;&mdash; на устройствах A и C)
      </p>
      <p>Устройство B может сделать запрос недостающей части 2 у обладающей ей устройств A и C, но выбирает устройство C, т.к. на устройстве
         C скачано меньше частей (1), чем у устройства A (2).
      </p>
      <p>Устройство C может сделать запрос недостающей части 1 у обладающей ей устройств A и B, но выбирает устройство B, т.к. на устройстве
         B скачано меньше частей (1), чем у устройства A (2).
      </p>
      <p>Во время третьего таймслота оба запроса оказываются единственными запросами у устройств B и C и удовлетворяются. Часть 2 передается
         с устройства C на устройство B. Часть 1 передается с устройства B на устройство C. Ценность устройства B для устройства C
         становится равной 1. Ценность устройства C для устройства B становится равной 1. 
      </p>
      <p>Все части обновления оказываются на всех устройствах и на этом обновление заканчивается.</p>
   </div>