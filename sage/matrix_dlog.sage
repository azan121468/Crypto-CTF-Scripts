#taked from https://icewizard4902.github.io/Cryptohack/the-matrix-reloaded/

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
