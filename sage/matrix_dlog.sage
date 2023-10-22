#taken from https://icewizard4902.github.io/Cryptohack/the-matrix-reloaded/

def solve_dlog(G, H):
    # useful for solving G ^ k = H
    R = IntegerModRing(P)
    M = MatrixSpace(R, N, N)
    g = M(G)
    h = M(H)

    g, p_mat = g.jordan_form(transformation=True)

    h = p_mat.inverse() * h * p_mat

    a11 = g[N - 2][N - 2]
    b11 = h[N - 2][N - 2]
    b12 = h[N - 2][N - 1]

    return (a11 * b12 / b11)


#simple code block to find x given w = G ^ x * v
#https://crypto.stackexchange.com/questions/3840/a-discrete-log-like-problem-with-matrices-given-ak-x-find-k

def find_matrix_power(G, v, w):
    jordan, p_mat = g.jordan_form(transformation=True)
    lam_bda = list(jordan)[-1][-1]
    p_inv_v = p_mat.inverse() * v
    p_inv_w = p_mat.inverse() * w
    x1, x2 = p_inv_v[-2], p_inv_v[-1]
    y1, y2 = p_inv_w[-2], p_inv_w[-1]
    
    k = lam_bda * (y1 - x1 * y2 / x2) / y2

    return k
