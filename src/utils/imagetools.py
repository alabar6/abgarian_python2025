import cv2
import matplotlib.pyplot as plt
import numpy as np


def read_image(path: str,
               rgb: bool = False,
               to_float: bool = False,
               shape: tuple[int, int] = None) -> np.ndarray:
    """
    Read image from ``path``

    Parameters
    ----------

    path : str

        Path to source image

        rgb : bool, optional

        If true, returns colored image in RGB. Else, return gray image. The default is False

        to_float : bool, optional

        If true, image's pixels will be integer numbers in range [0, ... 255]. Else, image's pixels will be 
        normalized in range [0, 1]. The default is False

        shape : tuple[int, int], optional

        Shape of image. If None, shape shape not changes. The default is None

    Returns
    -------

        img : np.ndarray

        Read image
    """

    if rgb:
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    else:
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if to_float:
        img = img / 255 

    if shape is not None:
        img = cv2.resize(img, (512, 512))

    return img

def plot_images(images: list[np.ndarray],
                titles: list[str] = None,
                figsize: tuple[int, int] = (10, 10),
                fontsize: int = 10,
                save_dir: str = None,
                save_title: str = None):
    """
    Show images from ``images`` list

    Parameters
    ----------

    images : list[np.ndarray]

    List of source images. Pixels value must be in [0, 1]

    titles : list[str], optional

    List of images titles. The default is None

    figsize : tuple[int, int]. optional

    Size of images. The default is (10, 10)

    fontsize : int, optional

    Size of font. The default is (10, 10)

    save_dir : str, optional

    If not None, image will be save in directory with path ``save_dir``. The default is None

    save_title : str, optional

    Title of saved image. If ``save_dir`` is not None, ``save_title`` also must be not None. The default is None
    """

    fig, axs = plt.subplots(nrows = 1, ncols = len(images), figsize = figsize)
    # axs = axs.ravel()

    for i, image in enumerate(images):
        axs[i].imshow(image, cmap='gray', vmin=0, vmax=1)
        # axs[i].axis('off')
        if titles is not None:
            axs[i].set_title(titles[i], fontsize=fontsize)

    plt.tight_layout()

    if save_dir is not None:
        assert save_title is not None, "Can't save image without title"
        plt.savefig(save_dir + save_title, bbox_inches = 'tight')

    plt.show()