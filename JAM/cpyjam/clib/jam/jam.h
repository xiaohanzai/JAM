/* -----------------------------------------------------------------------------
  JAM PROGRAMS
    
    jam_axi_rms_mgeint  : integrand for second moments
    jam_axi_rms_mmt     : second moments
    jam_axi_rms_wmmt    : weighted second moments
    jam_axi_vel_losint  : outer integrand for first moments
    jam_axi_vel_mgeint  : inner integrand for first moments
    jam_axi_vel_mmt     : first moments
    jam_axi_vel_wmmt    : weighted first moments
    jam_vel             : velocity vector structure
    params_losint       : parameter structure for first moment LOS integration
    params_mgeint       : parameter structure for first moment MGE integration
    params_rmsint       : parameter structure for second moment intergration
----------------------------------------------------------------------------- */


// definitions

#define True 1
#define False 0

#define AU  1.4959787068E8          // AU in km
#define G 0.00430237                // G in (km/s)^2 pc/Msun
#define RADEG 57.29578              // degrees per radian
#define RA2DEG 57.29578             // degrees per radian
#define pc2km  3.0856776e+13        // (km per parsec)


// ----------------------------------------------------------------------------


// structs

struct jam_vel {
    double *vx, *vy, *vz;
};

struct params_losint {
    struct multigaussexp *lum, *pot;
    double xp, yp, incl, *bani, *s2l, *q2l, *s2q2l, *s2p, *e2p, *kappa;
    double zpow;
};

struct params_mgeint {
    struct multigaussexp *lum, *pot;
    double r2, z2, *bani, *s2l, *q2l, *s2q2l, *s2p, *e2p, *knu;
};

struct params_rmsint {
    struct multigaussexp *lum, *pot;
    double *kani, *s2l, *q2l, *s2q2l, *s2p, *e2p;
    double x2, y2, xy, ci, si, ci2, si2, cisi;
    int vv;
};


// ----------------------------------------------------------------------------


// programs

double jam_axi_rms_mgeint( double, void * );

double* jam_axi_rms_mmt( double *,double *, int, double, \
    struct multigaussexp *, struct multigaussexp *, double *, \
    double, double, int, int, int );

double* jam_axi_rms_wmmt( double *, double *, int, double, \
    struct multigaussexp *, struct multigaussexp *, double *, int );

double jam_axi_vel_losint( double, void * );

double jam_axi_vel_mgeint( double, void * );

struct jam_vel jam_axi_vel_mmt( double *, double *, int, double, \
    struct multigaussexp *, struct multigaussexp *, double *, double *, \
    int, int );

double** jam_axi_vel_wmmt( double *, double *, int, double, \
    struct multigaussexp *, struct multigaussexp *, double *, double * );
