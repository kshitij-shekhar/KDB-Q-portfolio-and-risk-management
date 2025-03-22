// ✅ Core Trading Tables ✅ //

// Portfolios table
portfolios: (`portfolioID`name`owner`strategy) ! ((),(),(),()) // strategy field for quant models

// Holdings table (tracks open positions)
holdings: (`portfolioID`symbol`quantity`avg_price`mark_price`unrealized_pnl) ! ((),(),(),(),()) 

// Transactions table (captures all buy/sell orders)
transactions: (`txID`portfolioID`symbol`quantity`price`timestamp`order_type`exec_type`latency_ms) ! ((),(),(),(),(),(),(),()) 

// Market data (real-time price updates)
market_data: (`symbol`timestamp`bid`ask`last_price`volume`spread) ! ((),(),(),(),(),(),()) 

// Order book (level 2 market depth)
order_book: (`symbol`level`bid_price`ask_price`bid_size`ask_size`timestamp) ! ((),(),(),(),(),(),()) 

// Risk metrics (for risk analysis & margin calls)
risk_metrics: (`portfolioID`var_99`expected_shortfall`volatility`max_drawdown`leverage) ! ((),(),(),(),(),()) 

// Users table (Trader credentials & permissions)
users: (`userID`name`role) ! ((),(),()) 

// ✅ Execution & Performance Monitoring ✅ //

// Execution logs (trade speed analysis)
execution_logs: (`txID`execution_time`slippage`order_type`order_status`exchange_latency) ! ((),(),(),(),(),()) 

// Performance metrics (track PnL, Sharpe ratio)
performance_metrics: (`portfolioID`pnl`sharpe_ratio`sortino_ratio`alpha`beta) ! ((),(),(),(),(),()) 

// ✅ Liquidity & Capital Management ✅ //

// Cash balance per portfolio
cash_balance: (`portfolioID`cash_amount`currency) ! ((),(),()) 

// Margin accounts (track leverage usage)
margin_accounts: (`portfolioID`loan_amount`collateral_value`maintenance_margin`margin_call) ! ((),(),(),(),()) 

// Funding rates (for futures traders)
funding_rates: (`symbol`rate`timestamp) ! ((),(),()) 

// ✅ Advanced Data & Analytics ✅ //

// Economic events (e.g., interest rate decisions)
economic_events: (`event_name`date`impact_level`region) ! ((),(),(),()) 

// News sentiment (for market impact analysis)
news_sentiment: (`headline`timestamp`sentiment_score`source) ! ((),(),(),()) 

// Options chain data (Greeks & implied vol)
options_data: (`symbol`expiry_date`strike_price`option_type`iv`delta`gamma`theta`vega) ! ((),(),(),(),(),(),(),()) 

// ✅ Save tables to disk ✅ //
`:db/portfolios set portfolios
`:db/holdings set holdings
`:db/transactions set transactions
`:db/market_data set market_data
`:db/order_book set order_book
`:db/risk_metrics set risk_metrics
`:db/users set users
`:db/execution_logs set execution_logs
`:db/performance_metrics set performance_metrics
`:db/cash_balance set cash_balance
`:db/margin_accounts set margin_accounts
`:db/funding_rates set funding_rates
`:db/economic_events set economic_events
`:db/news_sentiment set news_sentiment
`:db/options_data set options_data
