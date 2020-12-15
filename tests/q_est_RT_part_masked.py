test = {
  'name': 'Question est_RT_part_masked',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'est_RT_part_masked'
          >>> 'est_RT_part_masked' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'est_RT_part_masked'
          >>> # from its initial state (of ...)
          >>> est_RT_part_masked is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 0 < est_RT_part_masked < 2.5
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          # masks = np.random.binomial(7, 0.125, size=(10000, int(10000 * 0.85)))
          # no_masks = np.random.binomial(7, 0.25, size=(10000, int(10000 * 0.15)))
          # res = np.c_[masks, no_masks]
          # means = np.mean(res, axis=1)
          # print(np.min(means), np.max(means))
          'code': r"""
          >>> 0.975 < est_RT_part_masked < 1.04
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
