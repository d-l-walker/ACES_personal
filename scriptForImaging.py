# ALMA Data Reduction Script

# Created using $Id: almaqa2isg.py,v 1.24 2021/10/27 09:52:59 dpetry Exp $

thesteps = []
step_title = {0: 'Transform SPW 25 for all MSs to common largest LSRK grid before concat',
              1: 'Transform SPW 27 for all MSs to common largest LSRK grid before concat',
              2: 'Transform SPW 29 for all MSs to common largest LSRK grid before concat',
              3: 'Transform SPW 31 for all MSs to common largest LSRK grid before concat',
              4: 'Transform SPW 33 for all MSs to common largest LSRK grid before concat',
              5: 'Transform SPW 35 for all MSs to common largest LSRK grid before concat',
              6: 'Concatenation of mstransformed MSs',
              7: 'Continuum image for target Sgr_A_star, spws [25, 27, 29, 31, 33, 35]',
              8: 'Continuum subtraction for field Sgr_A_star',
              9: 'Cube for target Sgr_A_star, spw 25',
              10: 'Cube for target Sgr_A_star, spw 27',
              11: 'Cube for target Sgr_A_star, spw 29',
              12: 'Cube for target Sgr_A_star, spw 31',
              13: 'Cube for target Sgr_A_star, spw 33',
              14: 'Cube for target Sgr_A_star, spw 35',
              15: 'Export images to FITS format'}

if 'applyonly' not in globals(): applyonly = False
try:
  print('List of steps to be executed ...'+str(mysteps))
  thesteps = mysteps
except:
  print('global variable mysteps not set.')
if (thesteps==[]):
  thesteps = range(0,len(step_title))
  print('Executing all steps: ', thesteps)

# The Python variable 'mysteps' will control which steps
# are executed when you start the script using
#   execfile('scriptForCalibration.py')
# e.g. setting
#   mysteps = [2,3,4]
# before starting the script will make the script execute
# only steps 2, 3, and 4
# Setting mysteps = [] will make it execute all steps.


import os
import sys

thevis = ['uid___A002_Xf8b429_Xa4c5.ms.split.cal',
          'uid___A002_Xf8f6a9_X216b.ms.split.cal']

# put restfreqs in this dictionary,
# one for each SPW ID, e.g. {17: '350GHz', 19: '356GHz'}
therestfreqs = {25: '86.2GHz',
                27: '86.9GHz',
                29: '89.188526GHz',
                31: '87.925237GHz',
                33: '98.6GHz',
                35: '100.5GHz'}

thevislsrk = ['uid___A002_Xf8b429_Xa4c5.ms.split.cal.lsrk.spw25',
              'uid___A002_Xf8b429_Xa4c5.ms.split.cal.lsrk.spw27',
              'uid___A002_Xf8b429_Xa4c5.ms.split.cal.lsrk.spw29',
              'uid___A002_Xf8b429_Xa4c5.ms.split.cal.lsrk.spw31',
              'uid___A002_Xf8b429_Xa4c5.ms.split.cal.lsrk.spw33',
              'uid___A002_Xf8b429_Xa4c5.ms.split.cal.lsrk.spw35',
              'uid___A002_Xf8f6a9_X216b.ms.split.cal.lsrk.spw25',
              'uid___A002_Xf8f6a9_X216b.ms.split.cal.lsrk.spw27',
              'uid___A002_Xf8f6a9_X216b.ms.split.cal.lsrk.spw29',
              'uid___A002_Xf8f6a9_X216b.ms.split.cal.lsrk.spw31',
              'uid___A002_Xf8f6a9_X216b.ms.split.cal.lsrk.spw33',
              'uid___A002_Xf8f6a9_X216b.ms.split.cal.lsrk.spw35']



# NOTE: the SPW IDs in the _image_names_ in this script use the numbering as in the original ASDM(s),
#       not the numbering used in the MS(s) processed directly by this script.
#       This is a requirement of the ALMA archive.

# Transform SPW 25 for all MSs to common largest LSRK grid before concat
mystep = 0
if(mystep in thesteps):
  casalog.post('Step '+str(mystep)+' '+step_title[mystep],'INFO')
  print('\nStep '+str(mystep)+' '+step_title[mystep])

  for myvis in thevis:
    os.system('rm -rf '+myvis+'.lsrk.spw25')
    mstransform(vis = myvis,
                outputvis = myvis+'.lsrk.spw25',
                outframe = 'LSRK',
                spw = '25',
                mode = 'frequency',
                nchan = 1918,
                width = '244.118kHz',
                start = '85.96399264500249GHz',
                regridms = True,
                datacolumn = 'data',
                reindex = True
                )
  

# Transform SPW 27 for all MSs to common largest LSRK grid before concat
mystep = 1
if(mystep in thesteps):
  casalog.post('Step '+str(mystep)+' '+step_title[mystep],'INFO')
  print('\nStep '+str(mystep)+' '+step_title[mystep])

  for myvis in thevis:
    os.system('rm -rf '+myvis+'.lsrk.spw27')
    mstransform(vis = myvis,
                outputvis = myvis+'.lsrk.spw27',
                outframe = 'LSRK',
                spw = '27',
                mode = 'frequency',
                nchan = 1918,
                width = '244.118kHz',
                start = '86.66392389073528GHz',
                regridms = True,
                datacolumn = 'data',
                reindex = True
                )
  

# Transform SPW 29 for all MSs to common largest LSRK grid before concat
mystep = 2
if(mystep in thesteps):
  casalog.post('Step '+str(mystep)+' '+step_title[mystep],'INFO')
  print('\nStep '+str(mystep)+' '+step_title[mystep])

  for myvis in thevis:
    os.system('rm -rf '+myvis+'.lsrk.spw29')
    mstransform(vis = myvis,
                outputvis = myvis+'.lsrk.spw29',
                outframe = 'LSRK',
                spw = '29',
                mode = 'frequency',
                nchan = 1914,
                width = '30.515kHz',
                start = '89.15731078473964GHz',
                regridms = True,
                datacolumn = 'data',
                reindex = True
                )
  

# Transform SPW 31 for all MSs to common largest LSRK grid before concat
mystep = 3
if(mystep in thesteps):
  casalog.post('Step '+str(mystep)+' '+step_title[mystep],'INFO')
  print('\nStep '+str(mystep)+' '+step_title[mystep])

  for myvis in thevis:
    os.system('rm -rf '+myvis+'.lsrk.spw31')
    mstransform(vis = myvis,
                outputvis = myvis+'.lsrk.spw31',
                outframe = 'LSRK',
                spw = '31',
                mode = 'frequency',
                nchan = 1914,
                width = '30.515kHz',
                start = '87.89412071674765GHz',
                regridms = True,
                datacolumn = 'data',
                reindex = True
                )
  

# Transform SPW 33 for all MSs to common largest LSRK grid before concat
mystep = 4
if(mystep in thesteps):
  casalog.post('Step '+str(mystep)+' '+step_title[mystep],'INFO')
  print('\nStep '+str(mystep)+' '+step_title[mystep])

  for myvis in thevis:
    os.system('rm -rf '+myvis+'.lsrk.spw33')
    mstransform(vis = myvis,
                outputvis = myvis+'.lsrk.spw33',
                outframe = 'LSRK',
                spw = '33',
                mode = 'frequency',
                nchan = 3838,
                width = '488.236kHz',
                start = '97.6630486223778GHz',
                regridms = True,
                datacolumn = 'data',
                reindex = True
                )
  

# Transform SPW 35 for all MSs to common largest LSRK grid before concat
mystep = 5
if(mystep in thesteps):
  casalog.post('Step '+str(mystep)+' '+step_title[mystep],'INFO')
  print('\nStep '+str(mystep)+' '+step_title[mystep])

  for myvis in thevis:
    os.system('rm -rf '+myvis+'.lsrk.spw35')
    mstransform(vis = myvis,
                outputvis = myvis+'.lsrk.spw35',
                outframe = 'LSRK',
                spw = '35',
                mode = 'frequency',
                nchan = 3838,
                width = '488.236kHz',
                start = '99.55832939457052GHz',
                regridms = True,
                datacolumn = 'data',
                reindex = True
                )
  

# Concatenation of mstransformed MSs
mystep = 6
if(mystep in thesteps):
  casalog.post('Step '+str(mystep)+' '+step_title[mystep],'INFO')
  print('\nStep '+str(mystep)+' '+step_title[mystep])

  os.system('rm -rf concat.ms')
  concat(vis = list(thevislsrk),
         concatvis = 'concat.ms',
         copypointing = False
         )
  
  

# Continuum image for target Sgr_A_star, spws [25, 27, 29, 31, 33, 35]
mystep = 7
if(mystep in thesteps):
  casalog.post('Step '+str(mystep)+' '+step_title[mystep],'INFO')
  print('\nStep '+str(mystep)+' '+step_title[mystep])

  
  os.system('rm -rf Sgr_A_star_sci.spw25_27_29_31_33_35.cont.I.manual*')
  tclean(vis = thevis,
         imagename = 'Sgr_A_star_sci.spw25_27_29_31_33_35.cont.I.manual',
         field = 'Sgr_A_star', # IDs from representative MS: '3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80'
         intent = 'OBSERVE_TARGET#ON_SOURCE',
         phasecenter = 45,
         stokes = 'I',
         spw = '25,27,29,31,33,35',
         outframe = 'LSRK',
         specmode = 'cont',
         nterms = 2,
         imsize = [1800, 5832],
         cell = '0.42arcsec',
         deconvolver = 'mtmfs',
         niter = 100,
         weighting = 'briggs',
         robust = 0.5,
         mask = '',
         gridder = 'mosaic',
         pbcor = True,
         threshold = '',
         interactive = True
         )
  
  # NOTE: enter the continuum channel selection in the spw parameter!
  
  os.system('mv Sgr_A_star_sci.spw25_27_29_31_33_35.cont.I.manual.image.tt0.pbcor Sgr_A_star_sci.spw25_27_29_31_33_35.cont.I.manual.image.pbcor')
  os.system('ln -sf Sgr_A_star_sci.spw25_27_29_31_33_35.cont.I.manual.image.pbcor Sgr_A_star_sci.spw25_27_29_31_33_35.cont.I.manual.image.tt0.pbcor')
  os.system('mv Sgr_A_star_sci.spw25_27_29_31_33_35.cont.I.manual.pb.tt0 Sgr_A_star_sci.spw25_27_29_31_33_35.cont.I.manual.pb')
  os.system('ln -sf Sgr_A_star_sci.spw25_27_29_31_33_35.cont.I.manual.pb Sgr_A_star_sci.spw25_27_29_31_33_35.cont.I.manual.pb.tt0')
  

# Continuum subtraction for field Sgr_A_star
mystep = 8
if(mystep in thesteps):
  casalog.post('Step '+str(mystep)+' '+step_title[mystep],'INFO')
  print('\nStep '+str(mystep)+' '+step_title[mystep])

  uvcontsub(vis = 'concat.ms',
            field = 'Sgr_A_star',
            spw = '0,1,2,3,4,5',
            fitspw = '<your channel selection here>',
            fitorder = 1,
            solint = 'int',
            combine = '',
            excludechans = False,
            want_cont = False
            )
  
  os.system('rm -rf concat.ms_Sgr_A_star.contsub')
  os.system('mv concat.ms.contsub concat.ms_Sgr_A_star.contsub')
  
  

# Cube for target Sgr_A_star, spw 25
mystep = 9
if(mystep in thesteps):
  casalog.post('Step '+str(mystep)+' '+step_title[mystep],'INFO')
  print('\nStep '+str(mystep)+' '+step_title[mystep])

  os.system('rm -rf Sgr_A_star_sci.spw25.cube.I.manual*')
  tclean(vis = 'concat.ms_Sgr_A_star.contsub',
         imagename = 'Sgr_A_star_sci.spw25.cube.I.manual',
         field = 'Sgr_A_star',
         intent = 'OBSERVE_TARGET#ON_SOURCE',
         phasecenter = 42,
         stokes = 'I',
         spw = '0',
         outframe = 'LSRK',
         restfreq = therestfreqs[25],
         specmode = 'cube',
         imsize = [1800, 5832],
         cell = '0.42arcsec',
         deconvolver = 'hogbom',
         niter = 100,
         weighting = 'briggsbwtaper',
         robust = 0.5,
         mask = '',
         gridder = 'mosaic',
         pbcor = True,
         threshold = '0.3mJy',
         width = 1,
         start = '', # native number of channels > 1000 (not taking into account width parameter)
         nchan = -1, # use ms.cvelfreqs to check; possibly constrain start and nchan to speed up processing
         interactive = True,
         perchanweightdensity = True
         )
  
  

# Cube for target Sgr_A_star, spw 27
mystep = 10
if(mystep in thesteps):
  casalog.post('Step '+str(mystep)+' '+step_title[mystep],'INFO')
  print('\nStep '+str(mystep)+' '+step_title[mystep])

  os.system('rm -rf Sgr_A_star_sci.spw27.cube.I.manual*')
  tclean(vis = 'concat.ms_Sgr_A_star.contsub',
         imagename = 'Sgr_A_star_sci.spw27.cube.I.manual',
         field = 'Sgr_A_star',
         intent = 'OBSERVE_TARGET#ON_SOURCE',
         phasecenter = 42,
         stokes = 'I',
         spw = '1',
         outframe = 'LSRK',
         restfreq = therestfreqs[27],
         specmode = 'cube',
         imsize = [1800, 5832],
         cell = '0.42arcsec',
         deconvolver = 'hogbom',
         niter = 100,
         weighting = 'briggsbwtaper',
         robust = 0.5,
         mask = '',
         gridder = 'mosaic',
         pbcor = True,
         threshold = '0.3mJy',
         width = 1,
         start = '', # native number of channels > 1000 (not taking into account width parameter)
         nchan = -1, # use ms.cvelfreqs to check; possibly constrain start and nchan to speed up processing
         interactive = True,
         perchanweightdensity = True
         )
  
  

# Cube for target Sgr_A_star, spw 29
mystep = 11
if(mystep in thesteps):
  casalog.post('Step '+str(mystep)+' '+step_title[mystep],'INFO')
  print('\nStep '+str(mystep)+' '+step_title[mystep])

  os.system('rm -rf Sgr_A_star_sci.spw29.cube.I.manual*')
  tclean(vis = 'concat.ms_Sgr_A_star.contsub',
         imagename = 'Sgr_A_star_sci.spw29.cube.I.manual',
         field = 'Sgr_A_star',
         intent = 'OBSERVE_TARGET#ON_SOURCE',
         phasecenter = 42,
         stokes = 'I',
         spw = '2',
         outframe = 'LSRK',
         restfreq = therestfreqs[29],
         specmode = 'cube',
         imsize = [1800, 5832],
         cell = '0.42arcsec',
         deconvolver = 'hogbom',
         niter = 100,
         weighting = 'briggsbwtaper',
         robust = 0.5,
         mask = '',
         gridder = 'mosaic',
         pbcor = True,
         threshold = '0.3mJy',
         width = 1,
         start = '', # native number of channels > 1000 (not taking into account width parameter)
         nchan = -1, # use ms.cvelfreqs to check; possibly constrain start and nchan to speed up processing
         interactive = True,
         perchanweightdensity = True
         )
  
  

# Cube for target Sgr_A_star, spw 31
mystep = 12
if(mystep in thesteps):
  casalog.post('Step '+str(mystep)+' '+step_title[mystep],'INFO')
  print('\nStep '+str(mystep)+' '+step_title[mystep])

  os.system('rm -rf Sgr_A_star_sci.spw31.cube.I.manual*')
  tclean(vis = 'concat.ms_Sgr_A_star.contsub',
         imagename = 'Sgr_A_star_sci.spw31.cube.I.manual',
         field = 'Sgr_A_star',
         intent = 'OBSERVE_TARGET#ON_SOURCE',
         phasecenter = 42,
         stokes = 'I',
         spw = '3',
         outframe = 'LSRK',
         restfreq = therestfreqs[31],
         specmode = 'cube',
         imsize = [1800, 5832],
         cell = '0.42arcsec',
         deconvolver = 'hogbom',
         niter = 100,
         weighting = 'briggsbwtaper',
         robust = 0.5,
         mask = '',
         gridder = 'mosaic',
         pbcor = True,
         threshold = '0.3mJy',
         width = 1,
         start = '', # native number of channels > 1000 (not taking into account width parameter)
         nchan = -1, # use ms.cvelfreqs to check; possibly constrain start and nchan to speed up processing
         interactive = True,
         perchanweightdensity = True
         )
  
  

# Cube for target Sgr_A_star, spw 33
mystep = 13
if(mystep in thesteps):
  casalog.post('Step '+str(mystep)+' '+step_title[mystep],'INFO')
  print('\nStep '+str(mystep)+' '+step_title[mystep])

  os.system('rm -rf Sgr_A_star_sci.spw33.cube.I.manual*')
  tclean(vis = 'concat.ms_Sgr_A_star.contsub',
         imagename = 'Sgr_A_star_sci.spw33.cube.I.manual',
         field = 'Sgr_A_star',
         intent = 'OBSERVE_TARGET#ON_SOURCE',
         phasecenter = 42,
         stokes = 'I',
         spw = '4',
         outframe = 'LSRK',
         restfreq = therestfreqs[33],
         specmode = 'cube',
         imsize = [1800, 5832],
         cell = '0.42arcsec',
         deconvolver = 'hogbom',
         niter = 100,
         weighting = 'briggsbwtaper',
         robust = 0.5,
         mask = '',
         gridder = 'mosaic',
         pbcor = True,
         threshold = '0.3mJy',
         width = 1,
         start = '', # native number of channels > 1000 (not taking into account width parameter)
         nchan = -1, # use ms.cvelfreqs to check; possibly constrain start and nchan to speed up processing
         interactive = True,
         perchanweightdensity = True
         )
  
  

# Cube for target Sgr_A_star, spw 35
mystep = 14
if(mystep in thesteps):
  casalog.post('Step '+str(mystep)+' '+step_title[mystep],'INFO')
  print('\nStep '+str(mystep)+' '+step_title[mystep])

  os.system('rm -rf Sgr_A_star_sci.spw35.cube.I.manual*')
  tclean(vis = 'concat.ms_Sgr_A_star.contsub',
         imagename = 'Sgr_A_star_sci.spw35.cube.I.manual',
         field = 'Sgr_A_star',
         intent = 'OBSERVE_TARGET#ON_SOURCE',
         phasecenter = 42,
         stokes = 'I',
         spw = '5',
         outframe = 'LSRK',
         restfreq = therestfreqs[35],
         specmode = 'cube',
         imsize = [1800, 5832],
         cell = '0.42arcsec',
         deconvolver = 'hogbom',
         niter = 100,
         weighting = 'briggsbwtaper',
         robust = 0.5,
         mask = '',
         gridder = 'mosaic',
         pbcor = True,
         threshold = '0.3mJy',
         width = 1,
         start = '', # native number of channels > 1000 (not taking into account width parameter)
         nchan = -1, # use ms.cvelfreqs to check; possibly constrain start and nchan to speed up processing
         interactive = True,
         perchanweightdensity = True
         )
  
  

# Export images to FITS format
mystep = 15
if(mystep in thesteps):
  casalog.post('Step '+str(mystep)+' '+step_title[mystep],'INFO')
  print('\nStep '+str(mystep)+' '+step_title[mystep])

  # NOTE: the SPW IDs in the image names in this script use the numbering as in the original ASDM(s)
  
  myimages = ['Sgr_A_star_sci.spw25.cube.I.manual',
              'Sgr_A_star_sci.spw25_27_29_31_33_35.cont.I.manual',
              'Sgr_A_star_sci.spw27.cube.I.manual',
              'Sgr_A_star_sci.spw29.cube.I.manual',
              'Sgr_A_star_sci.spw31.cube.I.manual',
              'Sgr_A_star_sci.spw33.cube.I.manual',
              'Sgr_A_star_sci.spw35.cube.I.manual']
  
  for myimagebase in myimages:
    exportfits(imagename = myimagebase+'.image.pbcor',
               fitsimage = myimagebase+'.pbcor.fits',
               overwrite = True
               )
    if os.path.exists(myimagebase+'.pb'):
      exportfits(imagename = myimagebase+'.pb',
                 fitsimage = myimagebase+'.pb.fits',
                 overwrite = True
                 )
  

