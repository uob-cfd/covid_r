test = {
  'name': 'Question est_RT_masked_ld',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'est_RT_masked_ld'
          >>> 'est_RT_masked_ld' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'est_RT_masked_ld'
          >>> # from its initial state (of ...)
          >>> est_RT_masked_ld is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 0 < est_RT_masked_ld < 2.5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          # res = np.random.binomial(7, 0.125, size=(10000, 10000))
          # means = np.mean(res, axis=1)
          # print(np.min(means), np.max(means))
          'code': r"""
          >>> 0.84 < est_RT_masked_ld < 0.91
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
