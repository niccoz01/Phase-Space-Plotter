import argparse
import PhaseSpacePlotter

# Add arguments to the parser
ap=argparse.ArgumentParser(description="Arguments for running the visualisation script")
ap.add_argument("--d", '--list', type=str, dest='der', nargs=2, help="List of the two ODEs", required=True)
ap.add_argument('--xmin', type=float, dest='xmin', help="Minimum value of x", default=-5)
ap.add_argument('--xmax', type=float, dest='xmax', help="Maximum value of x", default=5)
ap.add_argument('--ymin', type=float, dest='ymin', help="Minimum value of y", default=-5)
ap.add_argument('--ymax', type=float, dest='ymax', help="Maximum value of y", default=5)
ap.add_argument('--n', type=int, dest='n', help="Number of arrows", default=20)
ap.add_argument('--f', type=float, dest='F', help="Normalisation factor for the arrows", default=0.002)

pa = ap.parse_args()
der = pa.der
xmin = pa.xmin
xmax = pa.xmax
ymin = pa.ymin
ymax = pa.ymax
n = pa.n
F = pa.F

PhaseSpacePlotter.PSP(der, xmin, xmax, ymin, ymax, n, F)