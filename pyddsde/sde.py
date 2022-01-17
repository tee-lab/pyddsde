from collections import namedtuple
import numpy as np
from .fitters import PolyFit1D, PolyFit2D

class SDE:
    """
    A class to form a basic SDE from data

    Args
    ----
    X : array_like
            time series data
    t_int : float
            time step in time series
    Dt : int
            analysis time step
    inc : float
            max increment for binning thae data

    Returns
    -------
    diff : array_like
            diffusion in time series
    drift : array_like
            drift in time series
    avgdiff : array_like
            avarage diffusion
    avgdrift : array_like
            average drift

    :meta private:
    """

    def __init__(self, **kwargs):
        """
        pass

        .. document private functions
        """
        self.__dict__.update(kwargs)

    def _drift(self, X, t_int, Dt):
        r"""
        Get Drift coeffecient vector of data.

        Args
        ----
        X : array_like
                Time Series data
        t_int : float
                time difference betwen consecutive observations
        Dt : float
                drift calculation timescale

        Returns
        -------
        diff : array_like
            Diffusion in time series

        Notes
        -----
        Drift is calculated as follows

        .. math::
            drift = \frac{x(i+Dt)-x(i)}{tint * Dt}
        """

        # return np.array([b - a for a, b in zip(X, X[Dt:])]) / (t_int * Dt)
        return (X[Dt:] - X[:-Dt]) / (t_int * Dt)

    def _residual(self, X, t_int, Dt, dt=1):
        """
        Get the residual.
        """
        p = len(X) - max(dt, Dt)
        drift = self._drift(X, t_int, Dt)[:p]
        res = (X[dt:] - X[:-dt])[:p]
        return res - drift*(t_int*dt)

    def _diffusion_from_residual(self, X, F, t_int, dt=1):
        """
        Get diffusion using residuals about drift function.

        Parameters
        ----------
        X (np.array): Time-series
        t_int (float): Time-step
        F (Callable): Drift function
        """
        drift = F(X[:-dt])
        finite_diff = X[dt:] - X[:-dt]
        residual = finite_diff - drift * t_int
        return residual ** 2 / t_int

    def _diffusion(self, X, t_int, dt=1):
        """
        Get Diffusion coefficient vector of data

        Parameters
        ----------
        X : array_like
            time series data
        t_int : float
            time step in time series
        dt : int
            diffusion calculation timescale

        Returns
        --------
        diff : array.
            Diffusion
        """

        # return np.square(np.array([b - a for a, b in zip(X, X[dt:])])) / (t_int * dt)
        return np.square(X[dt:] - X[:-dt]) / (t_int * dt)

    def _diffusion_x_from_residual(self, x, y, A1, t_int, dt):
        drift = A1(x[:-dt], y[:-dt])
        finite_diff = x[dt:] - x[:-dt]
        residual = finite_diff - drift * t_int
        return residual ** 2 / t_int

    def _diffusion_y_from_residual(self, x, y, A2, t_int, dt):
        drift = A2(x[:-dt], y[:-dt])
        finite_diff = y[dt:] - y[:-dt]
        residual = finite_diff - drift * t_int
        return residual ** 2 / t_int

    def _diffusion_xy_from_residual(self, x, y, A1, A2, t_int, dt):
        drift_x = A1(x[:-dt], y[:-dt])
        drift_y = A2(x[:-dt], y[:-dt])
        residual_x = (x[dt:] - x[:dt]) - drift_x
        residual_y = (y[dt:] - y[:dt]) - drift_y
        return residual_x * residual_y / dt * t_int

    def _diffusion_xy(self, x, y, t_int, dt):
        """
        Get cross-correlation coefficients between x and y arrays.

        Args
        ----
        x : numpy.array
                x data
        y : numpy.array
                y data
        t_int : float
                time difference betwen consecutive observations
        dt : diffusion calculation timescale

        Returns
        -------
        diffusion_xy : numpy.array
                cross-correlation coefficients between x and y data
        """
        return ((x[dt:] - x[:-dt]) * (y[dt:] - y[:-dt])) / (dt * t_int)
        #return np.array([(b - a) * (d - c) for a, b, c, d in zip(x, x[dt:], y, y[dt:])]) / (dt * t_int)

    def _diffusion_yx(self, x, y, t_int, dt):
        """
        Get cross-correlation coefficients between x and y arrays.

        Args
        ----
        x : numpy.array
                x data
        y : numpy.array
                y data
        t_int : float
                time difference betwen consecutive observations
        dt : diffusion calculation timescale

        Returns
        -------
        diffusion_xy : numpy.array
                cross-correlation coefficients between y and x data
        """
        return ((x[dt:] - x[:-dt]) * (y[dt:] - y[:-dt])) / (dt * t_int)

    def _isValidRange(self, r):
        """
        Checks if the specified range of order parameter is valid range

        Args
        ----
        r : tuple, list
                range of order parameter

        Returns
        -------
        bool
                True if valid, False if not.
        """
        return isinstance(r, (list, tuple)) and len(r) == 2

    def _order_parameter(self, X, inc, r):
        """
        Get order parameter array for a given range and increments

        If range is None or not valid, order parameter array will be generated considering
        maxmium and mimimum limits of the data as the range

        Args
        ----
        X : numpy.array
                data
        inc : float
                step increments in order parameter
        r : tuple, list
                range of the order parameter

        Returns
        -------
        tuple
                first element will be the order parameter array
                second element is the rangen used
        """
        if r is None:
            r = (min(X), max(X))
        if not self._isValidRange(r):
            r = (min(X), max(X))
        if self.bins:
            #return np.linspace(min(X), max(X), self.bins)
            return np.linspace(r[0], r[-1], self.bins)
        return np.arange(min(r), max(r)+inc, inc)

    def _drift_and_diffusion(self, X, t_int, Dt, dt, inc):
        """
        Get drift and diffusion coefficients for a given timeseries data

        Args
        ----
        X : numpy.array
                time series data
        t_int : float
                time difference betwen consecutive observations
        Dt : int
                timescale to calculate drift
        dt : int
                timescale to claculate diffusion
        inc : float
                step increments in order parameter

        Returns
        -------
        diff : array
            diffusion of the data
        drift : array.
            drift, of the data
        avgdiff : array
            average diffusion
        avgdrift : array
            average drift 
        op : array
            order parameter
        """
        op = self._order_parameter(X, inc, self.op_range)
        avgdiff, avgdrift = [], []
        drift = self._drift(X, t_int, Dt)

        fitter = PolyFit1D()
        F = fitter.tune_and_fit(X[:-Dt], drift)
        diff = self._diffusion_from_residual(X, F, t_int, dt=dt)
        G = fitter.tune_and_fit(X[:-dt], diff)

        drift_ebar = []
        diff_ebar = []
        drift_num = []
        diff_num = []
        X = X[0 : -max(Dt, dt)]
        for b in op:
            i = np.where(np.logical_and(X < (b + inc), X >= b))[0]
            avgdiff.append(diff[i].mean())
            avgdrift.append(drift[i].mean())
            drift_ebar.append(drift[i].std()/np.sqrt(len(drift[i])))
            diff_ebar.append(diff[i].std()/np.sqrt(len(diff[i])))
            drift_num.append(len(drift[i]))
            diff_num.append(len(diff[i]))
        # return diff, drift, np.array(avgdiff), np.array(avgdrift), op, drift_ebar, diff_ebar, drift_num, diff_num, F, G
        DD = namedtuple('DD', 'diff drift avgdiff avgdrift op drift_ebar diff_ebar drift_num diff_num F G')
        return DD(
            diff=diff, drift=drift,
            avgdiff=np.array(avgdiff), avgdrift=np.array(avgdrift), op=op,
            drift_ebar=drift_ebar, diff_ebar=diff_ebar,
            drift_num=drift_num, diff_num=diff_num,
            F=F, G=G
        )

    def _vector_drift_diff(self, x, y, inc_x, inc_y, t_int, Dt, dt):
        """
        Get average binned drift and diffusion coefficients for given x and y data

        Args
        ----
        x : array_like
            timeseries x data
        y : array_like
            timesereis y data
        inc_x : float
            step increment of order parameter for x
        inc_y : float
            step increment of order parameter for y
        Dt : int
            timescale to calculate drift
        dt : int
            timescale to calculate diffusion

        Returns
        -------
        list
            [avgdriftX, avgdriftY, avgdiffX, avgdiffY, avgdiffXY, op_x, op_y]
        """

        fitter = PolyFit2D()

        op_x = self._order_parameter(x, inc_x, self.op_x_range)
        op_y = self._order_parameter(y, inc_y, self.op_y_range)

        driftX = self._drift(x, t_int, Dt)
        driftY = self._drift(y, t_int, Dt)

        v = np.stack((x[:-Dt], y[:-Dt]), axis=1)

        nan_idx = np.isnan(v).any(axis=1) | np.isnan(driftX) | np.isnan(driftY)
        v = v[~nan_idx]
        driftX_ = driftX[~nan_idx]
        driftY_ = driftY[~nan_idx]

        A1 = fitter.tune_and_fit(v, driftX_)
        A2 = fitter.tune_and_fit(v, driftY_)

        diffusionX = self._diffusion_x_from_residual(x, y, A1, t_int, dt)
        diffusionY = self._diffusion_y_from_residual(x, y, A1, t_int, dt)
        # diffusionX = self._diffusion(x, t_int, dt)
        # diffusionY = self._diffusion(y, t_int, dt)

        diffusionXY = self._diffusion_xy_from_residual(x, y, A1, A2, t_int, dt)
        diffusionYX = self._diffusion_xy_from_residual(x, y, A1, A2, t_int, dt)
        # diffusionXY = self._diffusion_xy(x, y, t_int, dt)
        # diffusionYX = self._diffusion_yx(x, y, t_int, dt)

        avgdriftX = np.zeros((len(op_x), len(op_y)))
        avgdriftY = np.zeros((len(op_x), len(op_y)))
        avgdiffX = np.zeros((len(op_x), len(op_y)))
        avgdiffY = np.zeros((len(op_x), len(op_y)))
        avgdiffXY = np.zeros((len(op_x), len(op_y)))
        avgdiffYX = np.zeros((len(op_x), len(op_y)))


        m = 0
        x_, y_ = x[0 : -max(Dt, dt)], y[0 : -max(Dt, dt)]
        for bin_x in op_y:
            n = 0
            for bin_y in op_x:
                i = np.where(
                    np.logical_and(
                        np.logical_and(x_ < (bin_x + inc_x), x_ >= bin_x),
                        np.logical_and(y_ < (bin_y + inc_y), y_ >= bin_y),
                    )
                )[0]
                avgdriftX[n, m] = np.nanmean(driftX[i])
                avgdriftY[n, m] = np.nanmean(driftY[i])
                avgdiffX[n, m] = np.nanmean(diffusionX[i])
                avgdiffY[n, m] = np.nanmean(diffusionY[i])
                avgdiffXY[n, m] = np.nanmean(diffusionXY[i])
                avgdiffYX[n, m] = np.nanmean(diffusionYX[i])
                n = n + 1
            m = m + 1
        return [avgdriftX, avgdriftY, avgdiffX, avgdiffY, avgdiffXY, avgdiffYX, op_x, op_y]

    def __call__(self, X, t_int, Dt, dt=1, inc=0.01, **kwargs):
        """
        Calcualtes drift, diffusion, average drift and avarage difussion.

        Parameters
        ----------
        X : list, array_like
                time series data
        t_int :float
                time step in time series
        Dt : float
                analysis time step
        inc = 0.01 : float
                max increment for binning thae data

        returns
        -------
        diff : array_like
                diffusion in time series
        drift : array_like
                drift in time series
        avgdiff : array_like
                avarage diffusion
        avgdrift : array_like
                avaerage drift
        """
        self.__dict__.update(kwargs)
        return self._drift_and_diffusion(X, t_int, Dt, inc)
