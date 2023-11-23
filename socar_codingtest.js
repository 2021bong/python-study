// 1번 문제
function solution(s) {
  let answer = [];
  const target = findTarget([...s]);
  let stack = [];
}

function findTarget(arrS) {
  const brkSLeft = arrS.filter((b) => b === '(');
  const brkSRight = arrS.filter((b) => b === ')');
  const brkMLeft = arrS.filter((b) => b === '{');
  const brkMRight = arrS.filter((b) => b === '}');
  const brkLLeft = arrS.filter((b) => b === '[');
  const brkLRight = arrS.filter((b) => b === ']');
  if (brkSLeft.length !== brkSRight.length) {
    return brkSLeft.length < brkSRight.length ? '(' : ')';
  } else if (brkMLeft.length !== brkMRight.length) {
    return brkMLeft.length < brkMRight.length ? '{' : '}';
  } else if (brkLLeft.length !== brkLRight.length) {
    return brkLLeft.length < brkLRight.length ? '[' : ']';
  }
}

// 2번 문제
// 시간 통과를 못할거같다는 생각이 있기는 함..
function solution(play_list, listen_time) {
  let answer = [];
  let listLength = play_list.length;
  for (let i = 0; i < listLength.length; i++) {
    if (i != 0) {
      let first = play_list.shift();
      play_list.push(first);
    }
    let restTime = listen_time;
    while (restTime > 0) {
      let count = 0;
      for (let i = 0; i < play_list.length; i++) {
        restTime -= 1;
        if (restTime >= 0) {
          count += 1;
          if (i === 0) {
            continue;
          } else if (i === play_list.length - 1) {
            answer.push(count);
          } else {
            restTime -= play_list[i] - 1;
          }
        } else {
          answer.push(count);
          break;
        }
      }
    }
  }
  return Math.max(...answer);
}
