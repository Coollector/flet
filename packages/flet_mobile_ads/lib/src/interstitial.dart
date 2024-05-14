import 'package:flet/flet.dart';
import 'package:flutter/widgets.dart';
import 'package:google_mobile_ads/google_mobile_ads.dart';

class InterstitialAdControl extends StatefulWidget {
  final Control? parent;
  final Control control;
  final FletControlBackend backend;

  const InterstitialAdControl(
      {super.key,
      required this.parent,
      required this.control,
      required this.backend});

  @override
  State<InterstitialAdControl> createState() => _InterstitialAdControlState();
}

class _InterstitialAdControlState extends State<InterstitialAdControl>
    with FletStoreMixin {
  InterstitialAd? _interstitialAd;
  bool _isLoaded = false;

  @override
  Widget build(BuildContext context) {
    debugPrint(
        "InterstitialAd build: ${widget.control.id} (${widget.control.hashCode})");
    return withPagePlatform((context, platform) {
      final testAdUnitId = platform == TargetPlatform.iOS
          ? 'ca-app-pub-3940256099942544/4411468910'
          : 'ca-app-pub-3940256099942544/1033173712';
      InterstitialAd.load(
          adUnitId: widget.control.attrString("unitId", testAdUnitId)!,
          request: const AdRequest(),
          adLoadCallback: InterstitialAdLoadCallback(
            // Called when an ad is successfully received.
            onAdLoaded: (ad) {
              ad.fullScreenContentCallback = FullScreenContentCallback(
                  // Called when the ad showed the full screen content.
                  onAdShowedFullScreenContent: (ad) {
                widget.backend.triggerControlEvent(widget.control.id, "open");
              },
                  // Called when an impression occurs on the ad.
                  onAdImpression: (ad) {
                widget.backend
                    .triggerControlEvent(widget.control.id, "impression");
              },
                  // Called when the ad failed to show full screen content.
                  onAdFailedToShowFullScreenContent: (ad, err) {
                widget.backend.triggerControlEvent(widget.control.id, "error");
                // Dispose the ad here to free resources.
                ad.dispose();
              },
                  // Called when the ad dismissed full screen content.
                  onAdDismissedFullScreenContent: (ad) {
                widget.backend.triggerControlEvent(widget.control.id, "close");
                // Dispose the ad here to free resources.
                ad.dispose();
              },
                  // Called when a click is recorded for an ad.
                  onAdClicked: (ad) {
                widget.backend.triggerControlEvent(widget.control.id, "click");
              });

              // Keep a reference to the ad so you can show it later.
              _interstitialAd = ad;
              widget.backend.triggerControlEvent(widget.control.id, "load");
            },
            // Called when an ad request failed.
            onAdFailedToLoad: (LoadAdError error) {
              debugPrint('InterstitialAd failed to load: $error');
              setState(() {
                _isLoaded = false;
              });
              _interstitialAd?.dispose();
            },
          ));

      () async {
        widget.backend.subscribeMethods(widget.control.id,
            (methodName, args) async {
          switch (methodName) {
            case "show":
              debugPrint("InterstitialAd.show($hashCode)");
              _interstitialAd?.show();
              return null;
          }
          return null;
        });
      }();

      return const SizedBox.shrink();
    });
  }
}
