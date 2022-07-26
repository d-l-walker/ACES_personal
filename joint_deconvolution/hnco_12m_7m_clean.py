import json, os, sys, glob

region      = sys.argv[1]
pth         = os.path.abspath(os.getcwd())

with open(f"./default_tclean_commands.json", "r") as fh:
    tclean_commands = json.load(fh)

os.chdir(pth+'/'+region)
if not os.path.exists('clean_12m_7m'):
    os.mkdir('clean_12m_7m')
os.chdir(pth+'/'+region+'/clean_12m_7m/')

vis_all     = glob.glob(pth+'/'+region+'/twelve_m/spws/*.spw3') + glob.glob(pth+'/'+region+'/seven_m/spws/*.spw3')
hnco_pars   = tclean_commands[region+'_TM1']['tclean_cube_pars']['spw31']

tclean(vis                     = vis_all,
       field                   = 'Sgr_A_star',
       datacolumn              = 'corrected',
       imagename               = region+'_12m_7m_SPW3.clean',
       specmode                = 'cube',
       gridder                 = 'mosaic',
       restoringbeam           = 'common',
       calcpsf                 = True,
       calcres                 = True,
       restoration             = True,
       pbcor                   = True,
       parallel                = True,
       interactive             = 0,
       cyclefactor             = 1.5,
       mosweight               = hnco_pars['mosweight'],
       outframe                = hnco_pars['outframe'],
       intent                  = hnco_pars['intent'],
       imsize                  = hnco_pars['imsize'],
       cell                    = hnco_pars['cell'],
       phasecenter             = hnco_pars['phasecenter'],
       perchanweightdensity    = hnco_pars['perchanweightdensity'],
       width                   = hnco_pars['width'],
       start                   = hnco_pars['start'],
       nchan                   = hnco_pars['nchan'],
       deconvolver             = hnco_pars['deconvolver'],
       weighting               = hnco_pars['weighting'],
       robust                  = hnco_pars['robust'],
       niter                   = hnco_pars['niter'],
       threshold               = hnco_pars['threshold'],
       usemask                 = hnco_pars['usemask'],
       sidelobethreshold       = hnco_pars['sidelobethreshold'],
       noisethreshold          = hnco_pars['noisethreshold'],
       lownoisethreshold       = hnco_pars['lownoisethreshold'],
       negativethreshold       = hnco_pars['negativethreshold'],
       minbeamfrac             = hnco_pars['minbeamfrac'],
       growiterations          = hnco_pars['growiterations'],
       dogrowprune             = hnco_pars['dogrowprune'])
