Feature: start task and measure time

  Scenario: User starts task
    Given user wants to start task
     When user pushes start task "Alice"
     Then timer starts
      And assistant says "Timing of Alice task started..."

  Scenario: User ends task
    Given user started task and wants to stop it
     When user pushes stop task "Alice"
     Then timer stops
      And assistant says "Timing of Alice task ended... \nIt took 3 hours."

