__author__ = 'aouyang1'

from util.strategy_functions import *

class FT_Quicky_Base:

    def __init__(self, backtest, PL, offset, FTdthresh, FTthresh, maxBars):
        self.bt = backtest
        self.PL = PL
        self.offset = offset
        self.FTdthresh = FTdthresh
        self.FTthresh = FTthresh
        self.maxBars = maxBars
        self.in_trend = False
        self.bars_passed = 0

    def on_bar_update(self):
        FT = self.bt.indicators['FisherTransform'].val
        FTd = self.bt.indicators['LinRegSlope'].val

        curr_bar_time = self.bt.range_bar.CloseTime[0].tz_localize('utc').tz_convert('US/Central')
        hod = curr_bar_time.hour
        entry_permitted = not(hod == 16 or hod == 17)

        if entry_permitted:
            if self.in_trend:
                if self.bt.market.position == 'FLAT':
                    if FT[0] > self.FTthresh:
                        if FTd[0] < -self.FTdthresh:
                            limit_price = self.bt.range_bar.Close[0]+self.offset*self.bt.range_bar.instr.TICK_SIZE
                            enter_short_limit(self.bt, limit_price)
                            set_profit_target(self.bt, self.PL)
                            set_stop_loss(self.bt, self.PL)
                            self.bt.market.position = "SHORT"
                            self.bars_passed = 0
                            self.bt.trades.curr.market_pos = self.bt.market.position
                            self.bt.trades.curr.entry_price = limit_price
                            #print "H{}, L{}, O{}, C{}".format(self.bt.range_bar.High[0],self.bt.range_bar.Low[0],self.bt.range_bar.Open[0],self.bt.range_bar.Close[0])
                            #print "go SHORT at {} @ {}".format(curr_bar_time, limit_price)

                    elif FT[0] < -self.FTthresh:
                        if FTd[0] > self.FTdthresh:
                            limit_price = self.bt.range_bar.Close[0]-self.offset*self.bt.range_bar.instr.TICK_SIZE
                            enter_long_limit(self.bt, limit_price)
                            set_profit_target(self.bt, self.PL)
                            set_stop_loss(self.bt, self.PL)
                            self.bt.market.position = "LONG"
                            self.bars_passed = 0
                            self.bt.trades.curr.market_pos = self.bt.market.position
                            self.bt.trades.curr.entry_price = limit_price
                            #print "H{}, L{}, O{}, C{}".format(self.bt.range_bar.High[0],self.bt.range_bar.Low[0],self.bt.range_bar.Open[0],self.bt.range_bar.Close[0])
                            #print "go LONG at {} @ {}".format(curr_bar_time, limit_price)


        if self.bt.order.order_state == "WORKING":
            self.bars_passed += 1
            if self.bars_passed > self.maxBars:
                cancel_order(self.bt)
                self.in_trend = False

        if cross_above(FT, self.FTthresh) or cross_below(FT, -self.FTthresh):
            self.in_trend = True
        elif cross_below(FT, self.FTthresh) or cross_above(FT, -self.FTthresh):
            self.in_trend = False

