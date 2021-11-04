# BJproblems


<!-- <details> -->
<summary>BJ_17069 : 파이프 옮기기 2</summary>

## __Notation__

$p_{ij}=[a_{ij},b_{ij},c_{ij}]^T$

각 좌표는 다음으로 표현하자 : $p_{00}=p_{ij}$ 라고 두면, 좌표는 $\begin{smallmatrix}p_{00}&p_{01}\\p_{10}&p_{11}\end{smallmatrix}$로 표현된다


$
\begin{bmatrix}a_{11} \\ b_{11} \\ c_{11}\end{bmatrix} =\begin{bmatrix}a_{01} & b_{01} & 0\\ a_{00}&b_{00} &c_{00}\\ 0&b_{10}&c_{10}\end{bmatrix} \begin{bmatrix}1\\1\\1\end{bmatrix}$

이후, position $i,j$ 에 벽이 있다면 $W_{ij}$ 를 곱한다
$\left(W_{01}=\left[\begin{smallmatrix}1&1&0\\1&1&1\\0&0&0\end{smallmatrix}\right] ,W_{10}=\left[\begin{smallmatrix}0&0&0\\1&1&1\\0&1&1\end{smallmatrix}\right] ,W_{00}=\left[\begin{smallmatrix}1&0&0\\0&0&0\\0&0&1\end{smallmatrix}\right]\right) $

</details>

