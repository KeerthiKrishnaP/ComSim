import matplotlib.pyplot as plt


def plot_hex(x, y):
    plt.plot(x, y)


def plot_circles(adsorbed_x, adsorbed_y, radius, width, my_dpi, n_pixels, figure_name, reference_indices=None):
    if reference_indices is None:
        reference_indices = []
    fig = plt.figure(figsize=(n_pixels / my_dpi, n_pixels / my_dpi), dpi=my_dpi)
    ax = fig.add_subplot(111)
    ax.set_aspect(1.0)

    plt.gca().set_axis_off()
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)

    for p in range(len(adsorbed_x)):
        ax.add_patch(
            plt.Circle(
                (adsorbed_x[p] - (width / 2), adsorbed_y[p] - (width / 2)),
                radius[p],
                color="k",
            )
        )

    # plt.savefig(figure_name, dpi=my_dpi, pad_inches = 0)
    # plt.show()
    return fig
